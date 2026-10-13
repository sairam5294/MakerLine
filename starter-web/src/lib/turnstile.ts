/**
 * Cloudflare Turnstile (free, privacy-friendly bot check). OFF until both keys are set:
 *   NEXT_PUBLIC_TURNSTILE_SITE_KEY (browser) and TURNSTILE_SECRET_KEY (server only).
 * The widget adds a hidden `cf-turnstile-response` field; the server verifies it here.
 */
const VERIFY_URL = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';

export const turnstileEnabled = () =>
  Boolean(process.env.TURNSTILE_SECRET_KEY && process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY);

export async function verifyTurnstile(
  token: string | null,
  ip: string | undefined,
  fetchImpl: typeof fetch = fetch,
): Promise<boolean> {
  if (!turnstileEnabled()) return true; // feature off → don't block
  if (!token) return false;
  const body = new FormData();
  body.set('secret', process.env.TURNSTILE_SECRET_KEY!);
  body.set('response', token);
  if (ip) body.set('remoteip', ip);
  try {
    const res = await fetchImpl(VERIFY_URL, {
      method: 'POST',
      body,
      signal: AbortSignal.timeout(5000),
    });
    const data = (await res.json()) as { success?: boolean };
    return data.success === true;
  } catch {
    return false; // fail closed: if we can't verify, don't accept (security standard A10)
  }
}
