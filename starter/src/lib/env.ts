import { z } from 'zod';

/**
 * Validates public environment variables once, at startup, so a missing/typo'd value
 * gives a clear message instead of a mysterious crash later.
 * Only EXPO_PUBLIC_* variables reach the app, and they are visible to anyone — no secrets.
 */
const schema = z.object({
  EXPO_PUBLIC_SUPABASE_URL: z.url(),
  EXPO_PUBLIC_SUPABASE_ANON_KEY: z.string().min(20),
  // Optional services: leave empty and the feature simply stays off.
  EXPO_PUBLIC_SENTRY_DSN: z.url().optional(),
  EXPO_PUBLIC_POSTHOG_KEY: z.string().min(10).optional(),
  EXPO_PUBLIC_POSTHOG_HOST: z.url().optional(),
});

export type PublicEnv = z.infer<typeof schema>;

export function readEnv(
  source: Record<string, string | undefined>,
): { ok: true; env: PublicEnv } | { ok: false; missing: string[] } {
  const result = schema.safeParse(source);
  if (result.success) return { ok: true, env: result.data };
  // Report variable names only — never values.
  return { ok: false, missing: result.error.issues.map((i) => String(i.path[0])) };
}

// Expo inlines EXPO_PUBLIC_* at build time, so each must be referenced literally.
export const env = readEnv({
  EXPO_PUBLIC_SUPABASE_URL: process.env.EXPO_PUBLIC_SUPABASE_URL,
  EXPO_PUBLIC_SUPABASE_ANON_KEY: process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY,
  EXPO_PUBLIC_SENTRY_DSN: process.env.EXPO_PUBLIC_SENTRY_DSN || undefined,
  EXPO_PUBLIC_POSTHOG_KEY: process.env.EXPO_PUBLIC_POSTHOG_KEY || undefined,
  EXPO_PUBLIC_POSTHOG_HOST: process.env.EXPO_PUBLIC_POSTHOG_HOST || undefined,
});

/** Optional service keys, readable even when Supabase isn't configured. */
export const optionalEnv = {
  sentryDsn: process.env.EXPO_PUBLIC_SENTRY_DSN || undefined,
  posthogKey: process.env.EXPO_PUBLIC_POSTHOG_KEY || undefined,
  posthogHost: process.env.EXPO_PUBLIC_POSTHOG_HOST || 'https://eu.i.posthog.com',
};
