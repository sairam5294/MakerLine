import { AxeBuilder } from '@axe-core/playwright';
import { expect, test } from '@playwright/test';

// Every route must pass automated WCAG 2.2 AA checks. Add new routes here.
for (const route of ['/', '/privacy']) {
  test(`${route} has no automatically detectable accessibility violations`, async ({ page }) => {
    await page.goto(route);
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();
    expect(results.violations.map((v) => `${v.id}: ${v.help}`)).toEqual([]);
  });
}

test('skip link is the first Tab stop and jumps to main content', async ({ page }) => {
  await page.goto('/');
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link', { name: 'Skip to content' })).toBeFocused();
});

test('strict CSP: no blocked scripts or styles on the page', async ({ page }) => {
  const violations: string[] = [];
  page.on('console', (msg) => {
    if (msg.type() === 'error' && /Content Security Policy|Refused to/i.test(msg.text()))
      violations.push(msg.text());
  });
  await page.goto('/');
  await page.getByLabel('Email').fill('sai@'); // interact so client JS must be running
  await page.getByRole('button', { name: 'Join the waitlist' }).click();
  await expect(page.locator('form').getByRole('alert')).toBeVisible();
  expect(violations).toEqual([]);
});
