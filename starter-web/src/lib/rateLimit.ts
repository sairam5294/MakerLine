/**
 * Simple fixed-window rate limiter (e.g. 5 sign-ups per IP per 10 minutes).
 * In-memory: good for one server or a small app. On serverless with many instances,
 * swap the Map for a shared store (Upstash Redis / a Supabase table) — same interface.
 */
export function createRateLimiter({
  limit,
  windowMs,
  now = () => Date.now(),
}: {
  limit: number;
  windowMs: number;
  now?: () => number;
}) {
  const hits = new Map<string, { count: number; resetAt: number }>();

  return function check(key: string): { ok: true } | { ok: false; retryAfterSec: number } {
    const t = now();
    const entry = hits.get(key);
    if (!entry || t >= entry.resetAt) {
      hits.set(key, { count: 1, resetAt: t + windowMs });
      return { ok: true };
    }
    if (entry.count < limit) {
      entry.count += 1;
      return { ok: true };
    }
    return { ok: false, retryAfterSec: Math.ceil((entry.resetAt - t) / 1000) };
  };
}
