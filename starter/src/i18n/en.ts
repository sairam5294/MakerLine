// English source strings. Every other language must have exactly the same keys (a test checks).
export const en = {
  home: {
    title: 'Welcome',
    body: 'Accessible components, design tokens, sign-in and tests are ready. Build your first feature from PLAN.md.',
    setupTitle: 'Setup needed',
    setupBody:
      'Copy .env.example to .env.local and add your Supabase URL and anon key. Missing: {{missing}}',
    signIn: 'Sign in',
    language: 'Language',
  },
  signIn: {
    title: 'Sign in',
    checkEmail: 'Check your email',
    email: 'Email',
    sendCode: 'Send code',
    codeSent: 'We sent a 6-digit code to {{email}}.',
    code: '6-digit code',
    verify: 'Verify and continue',
    differentEmail: 'Use a different email',
  },
  errors: {
    emailRequired: 'Enter your email address.',
    emailInvalid: 'Enter an email like name@example.com.',
    codeInvalid: 'Enter the 6-digit code from your email.',
    sendFailed: 'We couldn’t send the code. Check your connection and try again.',
    verifyFailed: 'That code didn’t work. Check it or request a new one.',
    notConfigured: 'Sign-in isn’t set up yet (missing Supabase keys).',
  },
  states: {
    loading: 'Loading',
    errorTitle: 'Something went wrong',
    errorBody: 'Please try again.',
    retry: 'Try again',
    offlineTitle: 'You’re offline',
    offlineBody: 'Check your connection, then try again.',
  },
};

// Deep "same shape, any string" type so translations can't miss or misspell a key.
type Shape<T> = { [K in keyof T]: T[K] extends string ? string : Shape<T[K]> };
export type Translation = Shape<typeof en>;
