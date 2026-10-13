import { describe, expect, it, vi } from 'vitest';

// Server actions read request headers; give tests a fake request (IP) instead.
vi.mock('next/headers', () => ({
  headers: async () =>
    new Headers({ 'x-forwarded-for': `10.0.0.${Math.floor(Math.random() * 250)}` }),
}));
import { joinWaitlist } from '@/app/actions';
import { initialWaitlistState, waitlistSchema } from '@/lib/waitlist';
import { themeCss } from '@/theme/cssVars';

const form = (fields: Record<string, string>) => {
  const fd = new FormData();
  for (const [k, v] of Object.entries(fields)) fd.set(k, v);
  return fd;
};

describe('waitlistSchema', () => {
  it.each([
    ['', 'Enter your email address.'],
    ['sai@', 'Enter an email like name@example.com.'],
  ])('%j → %s', (email, message) => {
    const r = waitlistSchema.safeParse({ email });
    expect(r.success).toBe(false);
    expect(r.error?.issues[0]?.message).toBe(message);
  });
});

describe('joinWaitlist', () => {
  it('returns the error and keeps what the user typed', async () => {
    const r = await joinWaitlist(initialWaitlistState, form({ email: 'nope' }));
    expect(r).toEqual({
      status: 'error',
      message: 'Enter an email like name@example.com.',
      email: 'nope',
    });
  });

  it('silently "succeeds" for bots that fill the honeypot', async () => {
    const r = await joinWaitlist(
      initialWaitlistState,
      form({ email: 'bot@x.io', company: 'spam' }),
    );
    expect(r.status).toBe('success');
  });

  it('says clearly when Supabase is not configured (never drops sign-ups silently)', async () => {
    delete process.env.SUPABASE_URL;
    const r = await joinWaitlist(initialWaitlistState, form({ email: 'sai@example.com' }));
    expect(r.status).toBe('error');
  });
});

describe('themeCss', () => {
  it('emits light and dark variables from tokens', () => {
    const css = themeCss();
    expect(css).toContain('--text-primary:');
    expect(css).toContain('prefers-color-scheme: dark');
  });
});
