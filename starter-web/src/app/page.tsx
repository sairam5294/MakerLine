import { headers } from 'next/headers';
import { WaitlistForm } from '@/components/WaitlistForm';

/**
 * Landing page for validate-idea: one promise, three benefits, one call to action.
 * Replace the copy with your value proposition from EVALUATION.md / VALIDATION.md.
 */
const benefits = [
  { title: 'Benefit one', body: 'The main outcome your user gets, in their own words.' },
  { title: 'Benefit two', body: 'What becomes easier or faster than their current workaround.' },
  { title: 'Benefit three', body: 'Why they can trust it — privacy, safety, quality.' },
];

export default async function Home() {
  const nonce = (await headers()).get('x-nonce') ?? undefined;
  return (
    <div className="flex flex-col gap-10">
      <header className="flex flex-col gap-4">
        <h1 className="text-4xl font-bold leading-tight">Your one-line promise goes here</h1>
        <p className="text-lg text-text-secondary">
          One or two sentences on who this is for and the problem it solves.
        </p>
      </header>

      <section aria-labelledby="benefits" className="flex flex-col gap-4">
        <h2 id="benefits" className="text-2xl font-semibold">
          Why it helps
        </h2>
        <ul className="grid gap-4 sm:grid-cols-3">
          {benefits.map((b) => (
            <li key={b.title} className="rounded-lg bg-surface p-4">
              <h3 className="font-semibold">{b.title}</h3>
              <p className="text-text-secondary">{b.body}</p>
            </li>
          ))}
        </ul>
      </section>

      <section aria-labelledby="join" className="flex flex-col gap-4">
        <h2 id="join" className="text-2xl font-semibold">
          Get early access
        </h2>
        <WaitlistForm
          nonce={nonce}
          turnstileSiteKey={process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY || undefined}
        />
      </section>
    </div>
  );
}
