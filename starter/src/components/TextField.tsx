import { useId } from 'react';
import { StyleSheet, Text, TextInput, View, type TextInputProps } from 'react-native';
import { minTouchTarget } from '@/theme/tokens';
import { useTheme } from '@/theme/useTheme';

type Props = Omit<TextInputProps, 'style'> & {
  /** Always-visible label (placeholders are not labels — they disappear while typing). */
  label: string;
  /** Error text shown under the field and announced to screen readers. */
  error?: string;
  hint?: string;
};

/** Labelled text input with error + hint support. */
export function TextField({ label, error, hint, ...inputProps }: Props) {
  const { colors, radius, space, type } = useTheme();
  const id = useId(); // Links the web <label> to the <input>.

  return (
    <View style={{ gap: space.xs }}>
      <Text nativeID={`${id}-label`} style={[type.label, { color: colors.textPrimary }]}>
        {label}
      </Text>
      <TextInput
        accessibilityLabel={label}
        // Screen readers read the hint/error after the label.
        accessibilityHint={error ?? hint}
        aria-labelledby={`${id}-label`}
        aria-invalid={Boolean(error)}
        placeholderTextColor={colors.textSecondary}
        style={[
          styles.input,
          type.body,
          {
            color: colors.textPrimary,
            backgroundColor: colors.background,
            // Error state uses colour AND text below (never colour alone).
            borderColor: error ? colors.danger : colors.border,
            borderRadius: radius.sm,
            paddingHorizontal: space.md,
          },
        ]}
        {...inputProps}
      />
      {error ? (
        // role="alert" makes screen readers announce the error as soon as it appears.
        <Text accessibilityRole="alert" style={[type.caption, { color: colors.danger }]}>
          {error}
        </Text>
      ) : hint ? (
        <Text style={[type.caption, { color: colors.textSecondary }]}>{hint}</Text>
      ) : null}
    </View>
  );
}

const styles = StyleSheet.create({
  input: { minHeight: minTouchTarget, borderWidth: 1 },
});
