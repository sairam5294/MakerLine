'use server';

import { createClient } from '@supabase/supabase-js';
import { headers } from 'next/headers';
import { createRateLimiter } from '@/lib/rateLimit';
import { verifyTurnstile } from '@/lib/turnstile';
import { waitlistSchema, type WaitlistState } from '@/lib/waitlist';

/**
 * Server action for the waitlist form. Runs on the server only, so validation can't be skipped.
 * Inserts with the SERVICE key, which exists only on the server (never NEXT_PUBLIC_…). The table
 * has RLS on and NO public policies, so bots can't bypass this form by calling the database API
 * directly with the public anon key. See supabase/migrations.
 */
// 5 attempts per visitor IP per 10 minutes stops scripted floods without bothering people.
const limitByIp = createRateLimiter({ limit: 5, windowMs: 10 * 60 * 1000 });

export async function joinWaitlist(
  _prev: WaitlistState,
  formData: FormData,
): Promise<WaitlistState> {
  const raw = {
    email: String(formData.get('email') ?? ''),
    company: String(formData.get('company') ?? ''),
  };
  const ip = (await headers()).get('x-forwarded-for')?.split(',')[0]?.trim();

  const limited = limitByIp(ip ?? 'unknown');
  if (!limited.ok) {
    return {
      status: 'error',
      message: `Too many attempts. Please try again in ${Math.ceil(limited.retryAfterSec / 60)} minutes.`,
      email: raw.email,
    };
  }

  if (!(await verifyTurnstile(formData.get('cf-turnstile-response') as string | null, ip))) {
    return {
      status: 'error',
      message: 'Please complete the “I’m human” check and try again.',
      email: raw.email,
    };
  }

  const parsed = waitlistSchema.safeParse(raw);

  if (!parsed.success) {
    // Honeypot filled → pretend success so bots don't learn anything.
    if (raw.company) return { status: 'success', message: 'Thanks! You’re on the list.' };
    return {
      status: 'error',
      message: parsed.error.issues[0]?.message ?? 'Check your email.',
      email: raw.email,
    };
  }

  const url = process.env.SUPABASE_URL;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY; // server-only secret
  if (!url || !serviceKey) {
    // Local preview without Supabase: behave normally but say so (never silently drop sign-ups in prod).
    return {
      status: 'error',
      message: 'The waitlist isn’t connected yet (missing Supabase keys).',
      email: raw.email,
    };
  }

  const supabase = createClient(url, serviceKey, { auth: { persistSession: false } });
  const { error } = await supabase
    .from('waitlist')
    .insert({ email: parsed.data.email.toLowerCase() });

  // 23505 = already on the list. Same friendly message, so we don't reveal who signed up.
  if (error && error.code !== '23505') {
    console.error('waitlist insert failed', error.code); // Code only — never log the email.
    return {
      status: 'error',
      message: 'Something went wrong. Please try again.',
      email: raw.email,
    };
  }
  return { status: 'success', message: 'Thanks! You’re on the list.' };
}
