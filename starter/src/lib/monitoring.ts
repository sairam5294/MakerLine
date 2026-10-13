import { optionalEnv } from './env';
import { scrubText } from './privacy';

/**
 * Crash & error reporting (Sentry). Does nothing until EXPO_PUBLIC_SENTRY_DSN is set.
 * Privacy: no IPs/cookies/user data (sendDefaultPii false) and emails/phones scrubbed from messages.
 * Performance: the Sentry SDK is loaded with a dynamic import() only when a DSN exists, so apps
 * without Sentry (and the web bundle's first load) don't pay for it.
 */
type SentryModule = typeof import('@sentry/react-native');
let sentry: Promise<SentryModule> | null = null;

export function initMonitoring() {
  if (!optionalEnv.sentryDsn) return;
  sentry = import('@sentry/react-native').then((Sentry) => {
    Sentry.init({
      dsn: optionalEnv.sentryDsn,
      sendDefaultPii: false,
      // Sample 20% of performance traces to stay inside the free tier; errors are always sent.
      tracesSampleRate: 0.2,
      enabled: !__DEV__, // Don't report errors from your own development sessions.
      beforeSend(event) {
        if (event.message) event.message = scrubText(event.message);
        for (const ex of event.exception?.values ?? []) {
          if (ex.value) ex.value = scrubText(ex.value);
        }
        delete event.user; // Never attach user identity.
        return event;
      },
    });
    return Sentry;
  });
}

/** Report a handled error (e.g. a failed API call you showed an error state for). */
export function reportError(error: unknown, context?: Record<string, string>) {
  sentry?.then((Sentry) => Sentry.captureException(error, { tags: context }));
}
