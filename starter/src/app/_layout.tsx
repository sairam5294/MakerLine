import '@/i18n'; // Load translations before any screen renders.
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { initMonitoring } from '@/lib/monitoring';
import { useTheme } from '@/theme/useTheme';

// Error reporting starts before the first screen (no-op without EXPO_PUBLIC_SENTRY_DSN).
initMonitoring();

/** Root layout: app-wide providers + the navigation stack. Every file in src/app is a screen. */
export default function RootLayout() {
  const { colors } = useTheme();
  const { t } = useTranslation();
  // One cache for server data (lists, profiles…). Created once per app launch.
  const [queryClient] = useState(
    () => new QueryClient({ defaultOptions: { queries: { retry: 2, staleTime: 30_000 } } }),
  );

  return (
    <QueryClientProvider client={queryClient}>
      <SafeAreaProvider>
        <StatusBar style="auto" />
        <Stack
          screenOptions={{
            headerStyle: { backgroundColor: colors.background },
            headerTintColor: colors.textPrimary,
            contentStyle: { backgroundColor: colors.background },
          }}
        >
          {/* Home shows its own large heading, so the bar is hidden to avoid a duplicate title. */}
          <Stack.Screen name="index" options={{ title: 'Home', headerShown: false }} />
          <Stack.Screen name="sign-in" options={{ title: t('signIn.title') }} />
        </Stack>
      </SafeAreaProvider>
    </QueryClientProvider>
  );
}
