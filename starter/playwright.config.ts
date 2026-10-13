import { defineConfig, devices } from '@playwright/test';

/**
 * End-to-end tests against the exported web build (npm run build:web → dist/).
 * Covers accessibility (axe) and critical flows. Mobile flows use Maestro (.maestro/).
 */
export default defineConfig({
  testDir: 'e2e',
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? [['html', { open: 'never' }], ['list']] : 'list',
  use: {
    baseURL: 'http://localhost:4173',
    trace: 'retain-on-failure',
    // Optional: point at an already-installed Chromium instead of downloading one.
    launchOptions: process.env.PW_CHROMIUM_PATH
      ? { executablePath: process.env.PW_CHROMIUM_PATH }
      : {},
  },
  projects: [
    { name: 'mobile-chrome', use: { ...devices['Pixel 7'] } }, // Most users are on phones.
    { name: 'desktop-chrome', use: { ...devices['Desktop Chrome'] } },
    // Safari engine: runs in CI (installed there) or locally with PW_WEBKIT=1.
    ...(process.env.CI || process.env.PW_WEBKIT
      ? [{ name: 'mobile-safari', use: { ...devices['iPhone 14'] } }]
      : []),
  ],
  webServer: {
    command: 'npx expo serve --port 4173',
    url: 'http://localhost:4173',
    reuseExistingServer: !process.env.CI,
    timeout: 60_000,
  },
});
