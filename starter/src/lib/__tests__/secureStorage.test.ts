import { CHUNK_SIZE, createChunkedStore } from '../secureStorage';

// In-memory fake store so the test runs without a device keychain.
function memoryStore() {
  const data = new Map<string, string>();
  return {
    data,
    getItem: async (k: string) => data.get(k) ?? null,
    setItem: async (k: string, v: string) => void data.set(k, v),
    removeItem: async (k: string) => void data.delete(k),
  };
}

describe('createChunkedStore', () => {
  it('round-trips values larger than one chunk', async () => {
    const mem = memoryStore();
    const store = createChunkedStore(mem);
    const big = 'a'.repeat(CHUNK_SIZE * 2 + 10);
    await store.setItem('session', big);
    expect(mem.data.get('session.count')).toBe('3');
    expect(await store.getItem('session')).toBe(big);
  });

  it('leaves no stale chunks when a shorter value replaces a longer one', async () => {
    const mem = memoryStore();
    const store = createChunkedStore(mem);
    await store.setItem('session', 'b'.repeat(CHUNK_SIZE * 3));
    await store.setItem('session', 'short');
    expect(await store.getItem('session')).toBe('short');
    expect(mem.data.has('session.1')).toBe(false);
  });

  it('returns null after removal (signed out)', async () => {
    const store = createChunkedStore(memoryStore());
    await store.setItem('session', 'x');
    await store.removeItem('session');
    expect(await store.getItem('session')).toBeNull();
  });
});
