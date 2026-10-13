import { useTranslation } from 'react-i18next';
import { ActivityIndicator, StyleSheet, Text, View } from 'react-native';
import { Button } from './Button';
import { useTheme } from '@/theme/useTheme';

/**
 * Standard non-content states so every screen handles them the same way
 * (UX standard: loading, empty, error, offline must all be designed).
 */
type Props =
  | { kind: 'loading'; message?: string }
  | { kind: 'empty'; title: string; message?: string; actionLabel?: string; onAction?: () => void }
  | { kind: 'error'; message?: string; onRetry: () => void }
  | { kind: 'offline'; onRetry: () => void };

export function ScreenState(props: Props) {
  const { colors, space, type } = useTheme();
  const { t } = useTranslation();
  const text = { color: colors.textPrimary };
  const sub = { color: colors.textSecondary };

  return (
    <View
      style={[styles.center, { padding: space.xl, gap: space.md }]}
      // Announce state changes (e.g. "Couldn't load") without moving focus.
      accessibilityLiveRegion="polite"
    >
      {props.kind === 'loading' && (
        <>
          <ActivityIndicator
            accessibilityLabel={props.message ?? t('states.loading')}
            color={colors.primary}
          />
          {props.message ? <Text style={[type.body, sub]}>{props.message}</Text> : null}
        </>
      )}

      {props.kind === 'empty' && (
        <>
          <Text accessibilityRole="header" style={[type.heading, text]}>
            {props.title}
          </Text>
          {props.message ? <Text style={[type.body, sub]}>{props.message}</Text> : null}
          {props.actionLabel && props.onAction ? (
            <Button label={props.actionLabel} onPress={props.onAction} />
          ) : null}
        </>
      )}

      {props.kind === 'error' && (
        <>
          <Text accessibilityRole="header" style={[type.heading, text]}>
            {t('states.errorTitle')}
          </Text>
          <Text style={[type.body, sub]}>{props.message ?? t('states.errorBody')}</Text>
          <Button label={t('states.retry')} onPress={props.onRetry} />
        </>
      )}

      {props.kind === 'offline' && (
        <>
          <Text accessibilityRole="header" style={[type.heading, text]}>
            {t('states.offlineTitle')}
          </Text>
          <Text style={[type.body, sub]}>{t('states.offlineBody')}</Text>
          <Button label={t('states.retry')} onPress={props.onRetry} />
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
});
