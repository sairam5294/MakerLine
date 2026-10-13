import { router } from 'expo-router';
import Head from 'expo-router/head';
import { useTranslation } from 'react-i18next';
import { Pressable, ScrollView, Text, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Button } from '@/components/Button';
import { languages } from '@/i18n';
import { env } from '@/lib/env';
import { minTouchTarget } from '@/theme/tokens';
import { useTheme } from '@/theme/useTheme';

/** Placeholder home screen — replace with your product's first screen. */
export default function Home() {
  const { colors, space, radius, type } = useTheme();
  const { t, i18n } = useTranslation();

  return (
    // Header is hidden on this screen, so keep content clear of the notch / status bar.
    <SafeAreaView style={{ flex: 1 }}>
      <ScrollView contentContainerStyle={{ padding: space.lg, gap: space.lg }}>
        {/* Browser tab title on web (WCAG 2.4.2 Page Titled). */}
        <Head>
          <title>{`${t('home.title')} · Starter`}</title>
        </Head>
        {/* accessibilityRole="header" lets screen-reader users jump between headings. */}
        <Text accessibilityRole="header" style={[type.title, { color: colors.textPrimary }]}>
          {t('home.title')}
        </Text>
        <Text style={[type.body, { color: colors.textSecondary }]}>{t('home.body')}</Text>

        {!env.ok && (
          // Setup help instead of a crash when .env.local is missing.
          <View
            accessibilityRole="alert"
            style={{ padding: space.md, backgroundColor: colors.surface, gap: space.xs }}
          >
            <Text style={[type.label, { color: colors.textPrimary }]}>{t('home.setupTitle')}</Text>
            <Text style={[type.body, { color: colors.textSecondary }]}>
              {t('home.setupBody', { missing: env.missing.join(', ') })}
            </Text>
          </View>
        )}

        <Button
          label={t('home.signIn')}
          onPress={() => router.push('/sign-in')}
          testID="home-sign-in"
        />

        {/* Language switcher: a radio group, so screen readers announce "selected". */}
        <View
          accessibilityRole="radiogroup"
          accessibilityLabel={t('home.language')}
          style={{ gap: space.sm }}
        >
          <Text style={[type.label, { color: colors.textPrimary }]}>{t('home.language')}</Text>
          <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: space.sm }}>
            {languages.map(({ code, label }) => {
              const selected = i18n.language === code;
              return (
                <Pressable
                  key={code}
                  accessibilityRole="radio"
                  // aria-checked (not accessibilityState) so web gets the attribute axe requires.
                  aria-checked={selected}
                  accessibilityLanguage={code}
                  onPress={() => i18n.changeLanguage(code)}
                  style={{
                    minHeight: minTouchTarget,
                    minWidth: minTouchTarget,
                    paddingHorizontal: space.md,
                    justifyContent: 'center',
                    borderRadius: radius.pill,
                    borderWidth: 2,
                    borderColor: selected ? colors.primary : colors.border,
                  }}
                >
                  <Text style={[type.label, { color: colors.textPrimary }]}>{label}</Text>
                </Pressable>
              );
            })}
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}
