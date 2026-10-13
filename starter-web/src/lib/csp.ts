/**
 * Content Security Policy with a fresh random nonce per request (no 'unsafe-inline' for scripts).
 * Only scripts/styles carrying the nonce may run, so injected code (XSS) is blocked.
 * Kept as a pure function so it's unit-tested (tests/security.test.ts).
 */
export const TURNSTILE_ORIGIN = 'https://challenges.cloudflare.com';

export function buildCsp(nonce: string, { dev = false, https = true } = {}): string {
  return [
    "default-src 'self'",
    // 'strict-dynamic' lets nonce'd scripts load their own chunks; dev needs eval for React debugging.
    `script-src 'self' 'nonce-${nonce}' 'strict-dynamic' ${TURNSTILE_ORIGIN}${dev ? " 'unsafe-eval'" : ''}`,
    `style-src 'self' 'nonce-${nonce}'`,
    "img-src 'self' blob: data:",
    "font-src 'self'",
    "connect-src 'self'",
    `frame-src ${TURNSTILE_ORIGIN}`, // Cloudflare Turnstile bot check (optional)
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'", // nobody can embed the site in an iframe (clickjacking)
    // Only on HTTPS: on plain http://localhost there is nothing to upgrade, and WebKit (Safari)
    // applies this directive to localhost too, which breaks fetch/server actions in local
    // and e2e runs (https://bugs.webkit.org/show_bug.cgi?id=250776).
    ...(https ? ['upgrade-insecure-requests'] : []),
  ].join('; ');
}

/** Unpredictable per-request nonce (Web Crypto works in the Next.js proxy/edge runtime). */
export function createNonce(): string {
  return btoa(crypto.randomUUID());
}
