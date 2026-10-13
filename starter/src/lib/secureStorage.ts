import * as SecureStore from 'expo-secure-store';
import { Platform } from 'react-native';

/**
 * Storage for the login session.
 * - iOS/Android: Keychain / Keystore via expo-secure-store (encrypted, per security standard).
 * - Web: localStorage (browsers have no keychain; keep web sessions short-lived).
 *
 * SecureStore values should stay under ~2 KB, but Supabase sessions can be larger,
 * so long values are split into numbered chunks: key.count, key.0, key.1, …
 */
export const CHUNK_SIZE = 1800;

type KeyValueStore = {
  getItem(key: string): Promise<string | null>;
  setItem(key: string, value: string): Promise<void>;
  removeItem(key: string): Promise<void>;
};

/** Adds chunking on top of any simple key-value store (exported for tests). */
export function createChunkedStore(store: KeyValueStore) {
  return {
    async getItem(key: string): Promise<string | null> {
      const count = await store.getItem(`${key}.count`);
      if (count === null) return null;
      const parts: string[] = [];
      for (let i = 0; i < Number(count); i++) {
        const part = await store.getItem(`${key}.${i}`);
        if (part === null) return null; // Corrupted/partial → treat as signed out.
        parts.push(part);
      }
      return parts.join('');
    },
    async setItem(key: string, value: string): Promise<void> {
      await this.removeItem(key); // Clear old chunks first so none are left behind.
      const count = Math.ceil(value.length / CHUNK_SIZE) || 1;
      for (let i = 0; i < count; i++) {
        await store.setItem(`${key}.${i}`, value.slice(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE));
      }
      await store.setItem(`${key}.count`, String(count));
    },
    async removeItem(key: string): Promise<void> {
      const count = await store.getItem(`${key}.count`);
      for (let i = 0; i < Number(count ?? 0); i++) await store.removeItem(`${key}.${i}`);
      await store.removeItem(`${key}.count`);
    },
  };
}

const nativeStore: KeyValueStore = {
  getItem: (k) => SecureStore.getItemAsync(k),
  setItem: (k, v) => SecureStore.setItemAsync(k, v),
  removeItem: (k) => SecureStore.deleteItemAsync(k),
};

const webStore: KeyValueStore = {
  // `typeof window` guard: static web export renders on the server where there's no storage.
  getItem: async (k) => (typeof window === 'undefined' ? null : window.localStorage.getItem(k)),
  setItem: async (k, v) => {
    if (typeof window !== 'undefined') window.localStorage.setItem(k, v);
  },
  removeItem: async (k) => {
    if (typeof window !== 'undefined') window.localStorage.removeItem(k);
  },
};

export const sessionStorage = createChunkedStore(Platform.OS === 'web' ? webStore : nativeStore);
