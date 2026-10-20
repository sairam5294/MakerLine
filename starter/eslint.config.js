// ESLint (flat config). Expo's recommended rules + a few MakerLine rules.
const { defineConfig } = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');

module.exports = defineConfig([
  expoConfig,
  { ignores: ['dist/*', '.expo/*', 'coverage/*', 'playwright-report/*', 'figma/*'] },
  {
    files: ['src/**/*.{ts,tsx}'],
    ignores: ['src/theme/**'],
    rules: {
      // Design tokens only: raw hex colours are allowed in src/theme and nowhere else.
      'no-restricted-syntax': [
        'error',
        {
          selector: 'Literal[value=/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/]',
          message: 'Use a design token from src/theme instead of a raw colour.',
        },
      ],
      // Leftover debug logs leak data and clutter production.
      'no-console': ['warn', { allow: ['warn', 'error'] }],
    },
  },
]);
