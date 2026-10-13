'use client';

import Link from 'next/link';
import Script from 'next/script';
import { useActionState, useId } from 'react';
import { joinWaitlist } from '@/app/actions';
import { initialWaitlistState } from '@/lib/waitlist';

type Props = {
  /** CSP nonce from the server (lets the Turnstile script run under the strict CSP). */
  nonce?: string;
  /** Cloudflare Turnstile site key; when absent the bot check is off. */
  turnstileSiteKey?: string;
};

/** Email sign-up with accessible label, error and success messages. Works without JavaScript too. */
export function WaitlistForm({ nonce, turnstileSiteKey }: Props) {
  const [state, formAction, pending] = useActionState(joinWaitlist, initialWaitlistState);
  const id = useId();
  const errorId = `${id}-error`;
  const hasError = state.status === 'error';

  if (state.status === 'success') {
    // role="status" announces the confirmation to screen readers without moving focus.
    return (
      <p role="status" className="rounded-lg bg-surface p-4 font-semibold text-success">
        {state.message}
      </p>
    );
  }

  return (
    <form action={formAction} noValidate className="flex flex-col gap-3">
      <label htmlFor={id} className="font-semibold">
        Email
      </label>
      <input
        id={id}
        name="email"
        type="email"
        autoComplete="email"
        inputMode="email"
        defaultValue={hasError ? state.email : ''} // Keep what the user typed after an error.
        aria-invalid={hasError}
        aria-describedby={hasError ? errorId : undefined}
        className={`min-h-11 rounded-md border bg-background px-4 text-base ${hasError ? 'border-danger' : 'border-border'}`}
      />
      {hasError && (
        // role="alert": read out immediately. Colour + text, never colour alone.
        <p id={errorId} role="alert" className="text-sm text-danger">
          {state.message}
        </p>
      )}
      {/* Honeypot — hidden from people and screen readers, visible to naive bots. */}
      <div aria-hidden="true" className="hidden">
        <label htmlFor={`${id}-company`}>Company</label>
        <input id={`${id}-company`} name="company" tabIndex={-1} autoComplete="off" />
      </div>
      {turnstileSiteKey && (
        <>
          {/* Bot check. Cloudflare's widget is keyboard- and screen-reader accessible. */}
          <Script
            src="https://challenges.cloudflare.com/turnstile/v0/api.js"
            strategy="afterInteractive"
            nonce={nonce}
          />
          <div className="cf-turnstile" data-sitekey={turnstileSiteKey} />
        </>
      )}
      <button
        type="submit"
        disabled={pending}
        aria-busy={pending}
        className="min-h-11 rounded-md bg-primary px-6 font-semibold text-text-on-primary hover:bg-primary-pressed disabled:opacity-60"
      >
        {pending ? 'Joining…' : 'Join the waitlist'}
      </button>
      <p className="text-sm text-text-secondary">
        We’ll only email you about the launch.{' '}
        <Link href="/privacy" className="underline">
          Privacy
        </Link>
      </p>
    </form>
  );
}
