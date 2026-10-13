/**
 * WCAG 2.x contrast ratio between two hex colours (e.g. '#1F5FD1', '#FFF').
 * Formula: (L1 + 0.05) / (L2 + 0.05) where L = relative luminance.
 * https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio
 */
function channel(value: number): number {
  const c = value / 255;
  // sRGB → linear light.
  return c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
}

function luminance(hex: string): number {
  let h = hex.replace('#', '');
  if (h.length === 3)
    h = h
      .split('')
      .map((ch) => ch + ch)
      .join(''); // #abc → #aabbcc
  const [r, g, b] = [0, 2, 4].map((i) => parseInt(h.slice(i, i + 2), 16));
  return 0.2126 * channel(r!) + 0.7152 * channel(g!) + 0.0722 * channel(b!);
}

export function contrastRatio(a: string, b: string): number {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi! + 0.05) / (lo! + 0.05);
}
