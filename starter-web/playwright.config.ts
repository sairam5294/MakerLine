import { defineConfig, devices } from '@playwright/test';

/** End-to-end + accessibility tests against the production build (npm run build first). */
export default defineConfig({
  testDir: 'e2e',
  retries: process.env.CI ? 1 : 0,
  reporter: process.env.CI ? [['html', { open: 'never' }], ['list']] : 'list',
  use: {
    baseURL: 'http://localhost:3100',
    trace: 'retain-on-failure',
    // Optional: point at an already-installed Chromium instead of downloading one.
    launchOptions: process.env.PW_CHROMIUM_PATH
      ? { executablePath: process.env.PW_CHROMIUM_PATH }
      : {},
  },
  projects: [
    { name: 'mobile-chrome', use: { ...devices['Pixel 7'] } },
    { name: 'desktop-chrome', use: { ...devices['Desktop Chrome'] } },
    // Safari engine: runs in CI (installed there) or locally with PW_WEBKIT=1.
    ...(process.env.CI || process.env.PW_WEBKIT
      ? [{ name: 'mobile-safari', use: { ...devices['iPhone 14'] } }]
      : []),
  ],
  webServer: {
    command: 'npx next start -p 3100',
    url: 'http://localhost:3100',
    reuseExistingServer: !process.env.CI,
    timeout: 60_000,
  },
});
