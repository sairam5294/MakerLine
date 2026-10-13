// Fails the build if any required colour pair drops below WCAG AA — in light or dark mode.
import { contrastRatio } from '../contrast';
import { contrastPairs, darkColors, lightColors } from '../tokens';

describe('contrastRatio', () => {
  it('matches known WCAG values', () => {
    expect(contrastRatio('#000000', '#FFFFFF')).toBeCloseTo(21, 1);
    expect(contrastRatio('#FFFFFF', '#FFFFFF')).toBeCloseTo(1, 5);
  });
});

describe.each([
  ['light', lightColors],
  ['dark', darkColors],
])('%s theme', (_name, colors) => {
  it.each(contrastPairs)('$fg on $bg ≥ $min:1', ({ fg, bg, min }) => {
    expect(contrastRatio(colors[fg], colors[bg])).toBeGreaterThanOrEqual(min);
  });
});
