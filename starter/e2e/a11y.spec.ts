import { AxeBuilder } from '@axe-core/playwright';
import { expect, test } from '@playwright/test';

// Every route must pass automated WCAG 2.2 AA checks. Add new routes to this list.
const routes = ['/', '/sign-in'];

for (const route of routes) {
  test(`${route} has no automatically detectable accessibility violations`, async ({ page }) => {
    await page.goto(route);
    await page.waitForLoadState('networkidle');
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .analyze();
    // Print a readable list if this fails, so the fix is obvious.
    expect(results.violations.map((v) => `${v.id}: ${v.help}`)).toEqual([]);
  });
}
