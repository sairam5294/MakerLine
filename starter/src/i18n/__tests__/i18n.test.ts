import i18n, { resources } from '../index';

// Collect every "a.b.c" key path in a translation object.
function keys(obj: object, prefix = ''): string[] {
  return Object.entries(obj).flatMap(([k, v]) =>
    typeof v === 'string' ? [`${prefix}${k}`] : keys(v as object, `${prefix}${k}.`),
  );
}
// Read a nested value by "a.b.c" path.
function get(obj: object, path: string): string {
  return path
    .split('.')
    .reduce<unknown>((o, k) => (o as Record<string, unknown>)[k], obj) as string;
}
function placeholders(text: string) {
  return (text.match(/{{\w+}}/g) ?? []).sort();
}

const english = resources.en.translation;

describe.each(Object.keys(resources).filter((l) => l !== 'en'))('%s translation', (lang) => {
  const tr = resources[lang as keyof typeof resources].translation;

  it('has exactly the same keys as English', () => {
    expect(keys(tr).sort()).toEqual(keys(english).sort());
  });

  it('keeps every {{placeholder}} and has no empty strings', () => {
    for (const key of keys(english)) {
      const en = i18n.t(key, { lng: 'en', interpolation: { skipOnVariables: true } }) as string;
      const other = get(tr, key);
      expect(other.trim()).not.toBe('');
      expect(placeholders(other)).toEqual(placeholders(get(english, key)));
      expect(en).toBeTruthy();
    }
  });
});

it('interpolates values', () => {
  expect(i18n.t('signIn.codeSent', { lng: 'hi', email: 'a@b.co' })).toContain('a@b.co');
});
