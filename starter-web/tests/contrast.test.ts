// Fails the build if any required colour pair drops below WCAG AA — in light or dark mode.
import { describe, expect, it } from 'vitest';
import { contrastRatio } from '@/theme/contrast';
import { contrastPairs, darkColors, lightColors } from '@/theme/tokens';

describe.each([
  ['light', lightColors],
  ['dark', darkColors],
])('%s theme', (_name, colors) => {
  it.each(contrastPairs)('$fg on $bg ≥ $min:1', ({ fg, bg, min }) => {
    expect(contrastRatio(colors[fg], colors[bg])).toBeGreaterThanOrEqual(min);
  });
});
