import { router, Stack } from 'expo-router';
import Head from 'expo-router/head';
import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { KeyboardAvoidingView, Platform, ScrollView, Text } from 'react-native';
import { Button } from '@/components/Button';
import { TextField } from '@/components/TextField';
import { validateEmail } from '@/features/auth/signInSchema';
import { track } from '@/lib/analytics';
import { reportError } from '@/lib/monitoring';
import { supabase } from '@/lib/supabase';
import { useTheme } from '@/theme/useTheme';

/**
 * Passwordless sign-in: email → 6-digit code.
 * Meets WCAG 3.3.8 (accessible authentication): no passwords to memorise, codes can be pasted
 * or auto-filled.
 */
type Step = 'email' | 'code';

export default function SignIn() {
  const { colors, space, type } = useTheme();
  const { t } = useTranslation();
  const [step, setStep] = useState<Step>('email');
  const [email, setEmail] = useState('');
  const [code, setCode] = useState('');
  // Holds a translation KEY (e.g. 'errors.emailInvalid'), shown with t() so it follows the language.
  const [errorKey, setErrorKey] = useState<string>();
  const [busy, setBusy] = useState(false);
  const title = step === 'email' ? t('signIn.title') : t('signIn.checkEmail');
  const error = errorKey ? t(errorKey) : undefined;

  async function sendCode() {
    const problem = validateEmail(email);
    setErrorKey(problem);
    if (problem) return; // Keep what the user typed; just show the message.
    if (!supabase) return setErrorKey('errors.notConfigured');

    setBusy(true);
    const { error: apiError } = await supabase.auth.signInWithOtp({ email: email.trim() });
    setBusy(false);
    if (apiError) {
      reportError(apiError, { step: 'send_code' }); // Email is never sent to error tracking.
      // Generic message: don't reveal whether an account exists (security standard).
      return setErrorKey('errors.sendFailed');
    }
    track('sign_in_code_sent');
    setStep('code');
  }

  async function verifyCode() {
    if (!/^\d{6}$/.test(code)) return setErrorKey('errors.codeInvalid');
    if (!supabase) return;

    setBusy(true);
    const { error: apiError } = await supabase.auth.verifyOtp({
      email: email.trim(),
      token: code,
      type: 'email',
    });
    setBusy(false);
    if (apiError) return setErrorKey('errors.verifyFailed');
    track('sign_in_completed');
    router.replace('/');
  }

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      style={{ flex: 1 }}
    >
      <ScrollView
        contentContainerStyle={{ padding: space.lg, gap: space.lg }}
        keyboardShouldPersistTaps="handled"
      >
        {/* One heading per screen: the navigation header shows the title, so the page doesn't
            repeat it (duplicate headings confuse screen-reader users). */}
        <Stack.Screen options={{ title }} />
        <Head>
          <title>{`${title} · Starter`}</title>
        </Head>

        {step === 'email' ? (
          <>
            <TextField
              label={t('signIn.email')}
              value={email}
              onChangeText={(v) => {
                setEmail(v);
                if (errorKey) setErrorKey(undefined); // Clear the error once the user starts fixing it.
              }}
              error={error}
              keyboardType="email-address"
              autoCapitalize="none"
              autoComplete="email"
              textContentType="emailAddress"
              returnKeyType="send"
              onSubmitEditing={sendCode}
              testID="email-input"
            />
            <Button
              label={t('signIn.sendCode')}
              onPress={sendCode}
              loading={busy}
              testID="send-code"
            />
          </>
        ) : (
          <>
            <Text style={[type.body, { color: colors.textSecondary }]}>
              {t('signIn.codeSent', { email: email.trim() })}
            </Text>
            <TextField
              label={t('signIn.code')}
              value={code}
              onChangeText={setCode}
              error={error}
              keyboardType="number-pad"
              autoComplete="one-time-code"
              textContentType="oneTimeCode"
              maxLength={6}
              testID="code-input"
            />
            <Button label={t('signIn.verify')} onPress={verifyCode} loading={busy} />
            <Button
              label={t('signIn.differentEmail')}
              variant="secondary"
              onPress={() => {
                setStep('email');
                setCode('');
                setErrorKey(undefined);
              }}
            />
          </>
        )}
      </ScrollView>
    </KeyboardAvoidingView>
  );
}
