import { useTranslation } from 'react-i18next';
import { useColorScheme } from 'react-native';
import { tallScriptLanguages, type Language } from '@/i18n';
import { darkColors, lightColors, radius, space, type } from './tokens';

/** Telugu/Devanagari glyphs are taller than Latin — give lines 20% more room to avoid clipping. */
const TALL_SCRIPT_LINE_HEIGHT = 1.2;

/** Returns the tokens for the user's light/dark setting and current language. */
export function useTheme() {
  const scheme = useColorScheme();
  const { i18n } = useTranslation();
  const colors = scheme === 'dark' ? darkColors : lightColors;

  const tall = tallScriptLanguages.includes(i18n.language as Language);
  const typeScale = tall
    ? (Object.fromEntries(
        Object.entries(type).map(([k, v]) => [
          k,
          { ...v, lineHeight: Math.round(v.lineHeight * TALL_SCRIPT_LINE_HEIGHT) },
        ]),
      ) as unknown as typeof type)
    : type;

  return { colors, space, radius, type: typeScale, scheme: scheme ?? 'light' };
}
