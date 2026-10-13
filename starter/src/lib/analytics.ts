import type PostHogClass from 'posthog-react-native';
import { optionalEnv } from './env';
import { sanitizeProps } from './privacy';

/**
 * Product analytics (PostHog), privacy-first:
 * - OFF until EXPO_PUBLIC_POSTHOG_KEY is set, and OFF for each user until they opt in.
 * - Event properties are sanitised (no emails, phones, names, free text).
 * - Children's apps: keep analytics OFF (DPDP bans tracking of under-18s; store kids rules).
 * - The SDK is loaded with a dynamic import() only when a key exists (smaller first load on web).
 * Use it only for the events listed in PRD.md → Analytics.
 */
let client: Promise<PostHogClass> | null = null;

function getClient(): Promise<PostHogClass> | null {
  if (!optionalEnv.posthogKey) return null;
  client ??= import('posthog-react-native').then(
    ({ default: PostHog }) =>
      new PostHog(optionalEnv.posthogKey!, {
        host: optionalEnv.posthogHost,
        defaultOptIn: false, // Opt-in: nothing is sent until setAnalyticsConsent(true).
        captureAppLifecycleEvents: false, // Only the events we choose, nothing automatic.
      }),
  );
  return client;
}

/** Call from your consent screen/settings toggle. */
export async function setAnalyticsConsent(allowed: boolean) {
  const ph = await getClient();
  if (!ph) return;
  if (allowed) await ph.optIn();
  else await ph.optOut();
}

/** Track a product event, e.g. track('lesson_completed', { lesson_id: 'l-12', minutes: 4 }). */
export function track(event: string, props?: Record<string, unknown>) {
  void getClient()?.then((ph) => ph.capture(event, sanitizeProps(props)));
}
