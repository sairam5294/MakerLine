import type { Metadata, Viewport } from 'next';
import { headers } from 'next/headers';
import { themeCss } from '@/theme/cssVars';
import './globals.css';

// Page title + description for search engines and link previews. Replace with your product.
export const metadata: Metadata = {
  title: { default: 'Starter — join the waitlist', template: '%s · Starter' },
  description: 'A one-page site to test demand: explain the idea, collect waitlist sign-ups.',
};

// Never block zoom (WCAG 1.4.4): no maximum-scale / user-scalable=no.
export const viewport: Viewport = { width: 'device-width', initialScale: 1 };

export default async function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  // Per-request nonce from src/proxy.ts. Reading headers makes pages render per request,
  // which strict CSP requires (static HTML can't carry a fresh nonce).
  const nonce = (await headers()).get('x-nonce') ?? undefined;
  return (
    // lang tells screen readers which voice/pronunciation to use (WCAG 3.1.1).
    <html lang="en">
      <head>
        {/* Theme colours from tokens.ts — one source of truth for light and dark mode. */}
        <style nonce={nonce} dangerouslySetInnerHTML={{ __html: themeCss() }} />
      </head>
      <body className="antialiased">
        {/* First Tab stop: jump past navigation straight to content (WCAG 2.4.1). */}
        <a
          href="#main"
          className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:rounded focus:bg-background focus:px-4 focus:py-2"
        >
          Skip to content
        </a>
        <main id="main" className="mx-auto max-w-2xl px-6 py-12">
          {children}
        </main>
      </body>
    </html>
  );
}
