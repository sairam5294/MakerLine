import { ActivityIndicator, Pressable, StyleSheet, Text } from 'react-native';
import { minTouchTarget } from '@/theme/tokens';
import { useTheme } from '@/theme/useTheme';

type Props = {
  /** Visible text. Also used as the screen-reader label unless `accessibilityLabel` is given. */
  label: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary';
  /** Shows a spinner and blocks double taps while an action runs. */
  loading?: boolean;
  disabled?: boolean;
  /** Extra context for screen readers, e.g. what happens after tapping. */
  accessibilityHint?: string;
  accessibilityLabel?: string;
  testID?: string;
};

/**
 * The one button component for the app. Accessibility is built in so screens can't forget it:
 * role=button, label, disabled/busy state, and a minimum 48×48 touch target.
 */
export function Button({
  label,
  onPress,
  variant = 'primary',
  loading = false,
  disabled = false,
  accessibilityHint,
  accessibilityLabel,
  testID,
}: Props) {
  const { colors, radius, space, type } = useTheme();
  const isPrimary = variant === 'primary';
  const inactive = disabled || loading;

  return (
    <Pressable
      accessibilityRole="button"
      accessibilityLabel={accessibilityLabel ?? label}
      accessibilityHint={accessibilityHint}
      // Tells VoiceOver/TalkBack the button is unavailable or working.
      accessibilityState={{ disabled: inactive, busy: loading }}
      disabled={inactive}
      onPress={onPress}
      testID={testID}
      style={({ pressed }) => [
        styles.base,
        {
          borderRadius: radius.md,
          paddingHorizontal: space.lg,
          backgroundColor: isPrimary
            ? pressed
              ? colors.primaryPressed
              : colors.primary
            : 'transparent',
          borderColor: colors.primary,
          opacity: inactive ? 0.6 : 1,
        },
      ]}
    >
      {loading ? (
        // Spinner is decorative; the busy state above is what screen readers announce.
        <ActivityIndicator color={isPrimary ? colors.textOnPrimary : colors.primary} />
      ) : (
        <Text style={[type.label, { color: isPrimary ? colors.textOnPrimary : colors.primary }]}>
          {label}
        </Text>
      )}
    </Pressable>
  );
}

const styles = StyleSheet.create({
  base: {
    minHeight: minTouchTarget,
    minWidth: minTouchTarget,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 2,
  },
});
