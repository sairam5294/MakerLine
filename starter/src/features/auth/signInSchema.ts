import { z } from 'zod';

/**
 * Sign-in form rules. Messages are translation KEYS (see src/i18n/en.ts) so every language
 * gets a plain, specific message that says how to fix the problem.
 */
export const signInSchema = z.object({
  email: z.string().trim().min(1, 'errors.emailRequired').pipe(z.email('errors.emailInvalid')),
});

export type SignInValues = z.infer<typeof signInSchema>;

/** Returns the translation key of the first email error, or undefined if valid. */
export function validateEmail(email: string): string | undefined {
  const result = signInSchema.safeParse({ email });
  return result.success ? undefined : result.error.issues[0]?.message;
}
