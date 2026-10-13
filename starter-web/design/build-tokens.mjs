#!/usr/bin/env node
/**
 * Design tokens → code. Reads design/tokens.json (W3C Design Tokens format, the single source
 * of truth shared with Figma) and writes src/theme/tokens.generated.ts for the app.
 *
 *   node design/build-tokens.mjs          → write the generated file
 *   node design/build-tokens.mjs --check  → fail if the generated file is out of date (used in CI)
 *
 * No dependencies on purpose: works in any project with Node.
 */
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const tokens = JSON.parse(readFileSync(join(root, 'design/tokens.json'), 'utf8'));
const outFile = join(root, 'src/theme/tokens.generated.ts');

// Follow "{color.palette.blue600}"-style references to their final value.
function resolve(value, seen = new Set()) {
  if (typeof value !== 'string' || !value.startsWith('{')) return value;
  const path = value.slice(1, -1);
  if (seen.has(path)) throw new Error(`Circular token reference: ${path}`);
  seen.add(path);
  const node = path.split('.').reduce((o, k) => o?.[k], tokens);
  if (!node || !('$value' in node)) throw new Error(`Unknown token reference: ${value}`);
  return resolve(node.$value, seen);
}

// "{…}"-free map of a token group: { name: resolvedValue }
const group = (obj) =>
  Object.fromEntries(Object.entries(obj).filter(([k]) => !k.startsWith('$')).map(([k, v]) => [k, resolve(v.$value)]));
const px = (v) => Number(String(v).replace('px', ''));
const ms = (v) => Number(String(v).replace('ms', ''));
const mapValues = (o, f) => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, f(v)]));

const light = group(tokens.color.light);
const dark = group(tokens.color.dark);
// Every colour must exist in both themes, otherwise one theme would silently fall back.
const missing = Object.keys(light).filter((k) => !(k in dark)).concat(Object.keys(dark).filter((k) => !(k in light)));
if (missing.length) throw new Error(`Colour tokens missing in one theme: ${missing.join(', ')}`);

const typography = mapValues(group(tokens.typography), (t) => ({
  fontSize: px(t.fontSize),
  lineHeight: px(t.lineHeight),
  fontWeight: String(t.fontWeight),
}));

const out = `// ⚠️ GENERATED from design/tokens.json by design/build-tokens.mjs — do not edit by hand.
// Change tokens.json (or sync it from Figma), then run: npm run tokens

export const palette = ${JSON.stringify(group(tokens.color.palette), null, 2)} as const;

export type SemanticColor = ${Object.keys(light).map((k) => `'${k}'`).join(' | ')};
export type ColorTokens = Record<SemanticColor, string>;

export const lightColors: ColorTokens = ${JSON.stringify(light, null, 2)};

export const darkColors: ColorTokens = ${JSON.stringify(dark, null, 2)};

export const space = ${JSON.stringify(mapValues(group(tokens.space), px), null, 2)} as const;

export const radius = ${JSON.stringify(mapValues(group(tokens.radius), px), null, 2)} as const;

export const type = ${JSON.stringify(typography, null, 2)} as const;

export const minTouchTarget = ${px(resolve(tokens.size.minTouchTarget.$value))};

export const motion = ${JSON.stringify(mapValues(group(tokens.duration), ms), null, 2)} as const;

/** Colour pairs that must pass WCAG 2.2 AA (4.5 = text, 3 = large text / UI boundaries). */
export const contrastPairs: { fg: SemanticColor; bg: SemanticColor; min: number }[] = ${JSON.stringify(
  tokens.$extensions.productKit.contrastPairs,
  null,
  2,
)};
`;

if (process.argv.includes('--check')) {
  const current = existsSync(outFile) ? readFileSync(outFile, 'utf8') : '';
  if (current !== out) {
    console.error('✖ src/theme/tokens.generated.ts is out of date. Run: npm run tokens');
    process.exit(1);
  }
  console.log('✔ tokens up to date');
} else {
  writeFileSync(outFile, out);
  console.log('✔ wrote src/theme/tokens.generated.ts');
}
