import { z } from 'zod';

/** Waitlist form rules. Messages are shown to users: plain, specific, and say how to fix it. */
export const waitlistSchema = z.object({
  email: z
    .string()
    .trim()
    .min(1, 'Enter your email address.')
    .max(254, 'That email is too long.')
    .pipe(z.email('Enter an email like name@example.com.')),
  // Hidden "honeypot" field: people never see it, simple bots fill it in.
  company: z.string().max(0).optional(),
});

export type WaitlistState =
  | { status: 'idle' }
  | { status: 'error'; message: string; email: string }
  | { status: 'success'; message: string };

export const initialWaitlistState: WaitlistState = { status: 'idle' };
