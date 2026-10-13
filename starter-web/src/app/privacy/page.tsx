import type { Metadata } from 'next';
import Link from 'next/link';

export const metadata: Metadata = { title: 'Privacy' };

/** Plain-language privacy notice for the waitlist. Have it reviewed before a real launch. */
export default function Privacy() {
  return (
    <article className="flex flex-col gap-4">
      <h1 className="text-3xl font-bold">Privacy</h1>
      <p>We collect only your email address, to tell you when we launch.</p>
      <p>
        We don’t sell it, share it, or use it for ads. It’s stored with our database provider
        (Supabase).
      </p>
      <p>
        To be removed, email{' '}
        <a className="underline" href="mailto:hello@example.com">
          hello@example.com
        </a>{' '}
        and we’ll delete it within 7 days.
      </p>
      <p>
        <Link className="underline" href="/">
          Back to home
        </Link>
      </p>
    </article>
  );
}
