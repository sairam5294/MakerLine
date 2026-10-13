import { darkColors, lightColors, type ColorTokens } from './tokens';

/** "textPrimary" → "--text-primary" */
const toVar = (name: string) => `--${name.replace(/[A-Z]/g, (c) => `-${c.toLowerCase()}`)}`;

const block = (colors: ColorTokens) =>
  Object.entries(colors)
    .map(([name, value]) => `${toVar(name)}:${value};`)
    .join('');

/**
 * Builds the CSS custom properties for light + dark themes from tokens.ts, so colours have ONE
 * source of truth. Injected in layout.tsx; Tailwind reads them via @theme in globals.css.
 */
export function themeCss(): string {
  return `:root{${block(lightColors)}color-scheme:light dark;}@media (prefers-color-scheme: dark){:root{${block(darkColors)}}}`;
}
