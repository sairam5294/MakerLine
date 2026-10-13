import { afterEach, describe, expect, it, vi } from 'vitest';
import { buildCsp, createNonce } from '@/lib/csp';
import { createRateLimiter } from '@/lib/rateLimit';
import { verifyTurnstile } from '@/lib/turnstile';

describe('buildCsp', () => {
  it('allows only nonce-carrying scripts in production (no unsafe-inline / unsafe-eval)', () => {
    const csp = buildCsp('abc');
    expect(csp).toContain("script-src 'self' 'nonce-abc' 'strict-dynamic'");
    expect(csp).not.toContain('unsafe-inline');
    expect(csp).not.toContain('unsafe-eval');
    expect(csp).toContain("frame-ancestors 'none'");
  });
  it('adds unsafe-eval only in development', () => {
    expect(buildCsp('abc', { dev: true })).toContain("'unsafe-eval'");
  });
  it('creates a different nonce every time', () => {
    expect(createNonce()).not.toBe(createNonce());
  });
});

describe('createRateLimiter', () => {
  it('allows `limit` hits per window, then blocks until the window resets', () => {
    let t = 0;
    const check = createRateLimiter({ limit: 2, windowMs: 1000, now: () => t });
    expect(check('ip').ok).toBe(true);
    expect(check('ip').ok).toBe(true);
    expect(check('ip')).toEqual({ ok: false, retryAfterSec: 1 });
    expect(check('other-ip').ok).toBe(true); // separate visitors are independent
    t = 1000;
    expect(check('ip').ok).toBe(true);
  });
});

describe('verifyTurnstile', () => {
  afterEach(() => {
    delete process.env.TURNSTILE_SECRET_KEY;
    delete process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY;
  });
  const enable = () => {
    process.env.TURNSTILE_SECRET_KEY = 'secret';
    process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY = 'site';
  };
  it('is a no-op when keys are not configured', async () => {
    expect(await verifyTurnstile(null, undefined)).toBe(true);
  });
  it('rejects a missing token when enabled', async () => {
    enable();
    expect(await verifyTurnstile(null, '1.2.3.4')).toBe(false);
  });
  it('accepts when Cloudflare says success', async () => {
    enable();
    const fakeFetch = vi.fn(async () => new Response(JSON.stringify({ success: true })));
    expect(await verifyTurnstile('tok', '1.2.3.4', fakeFetch as unknown as typeof fetch)).toBe(
      true,
    );
  });
  it('fails closed on network errors', async () => {
    enable();
    const failing = vi.fn(async () => {
      throw new Error('offline');
    });
    expect(await verifyTurnstile('tok', undefined, failing as unknown as typeof fetch)).toBe(false);
  });
});
