import { AxeBuilder } from '@axe-core/playwright';
import { expect, test } from '@playwright/test';

// Switching language updates the UI, is announced as a selected radio, and stays accessible.
test('switch to Telugu and Hindi', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('radio', { name: 'తెలుగు' }).click();
  await expect(page.getByRole('heading', { name: 'స్వాగతం' })).toBeVisible();
  await expect(page.getByRole('radio', { name: 'తెలుగు' })).toHaveAttribute('aria-checked', 'true');

  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag22aa'])
    .analyze();
  expect(results.violations.map((v) => v.id)).toEqual([]);

  await page.getByRole('radio', { name: 'हिन्दी' }).click();
  await expect(page.getByRole('heading', { name: 'स्वागत है' })).toBeVisible();
});
