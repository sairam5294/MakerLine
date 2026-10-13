import { readEnv } from '../env';

describe('readEnv', () => {
  it('accepts valid public config', () => {
    const r = readEnv({
      EXPO_PUBLIC_SUPABASE_URL: 'https://abc.supabase.co',
      EXPO_PUBLIC_SUPABASE_ANON_KEY: 'x'.repeat(40),
    });
    expect(r.ok).toBe(true);
  });

  it('reports missing variable NAMES only (never values)', () => {
    const r = readEnv({ EXPO_PUBLIC_SUPABASE_URL: 'not-a-url' });
    expect(r).toEqual({
      ok: false,
      missing: ['EXPO_PUBLIC_SUPABASE_URL', 'EXPO_PUBLIC_SUPABASE_ANON_KEY'],
    });
  });
});
