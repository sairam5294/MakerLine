import path from 'node:path';
import { defineConfig } from 'vitest/config';

// Unit tests (pure logic). Browser flows + accessibility live in e2e/ (Playwright).
export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      // 'server-only' throws outside Next's server build; in unit tests treat it as empty.
      'server-only': path.resolve(__dirname, 'tests/empty-module.ts'),
    },
  },
  test: { include: ['tests/**/*.test.ts'], environment: 'node' },
});
