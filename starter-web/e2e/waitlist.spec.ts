import { expect, test } from '@playwright/test';

test('invalid email shows an announced error and keeps the typed value', async ({ page }) => {
  await page.goto('/');
  const email = page.getByLabel('Email');
  await email.fill('sai@');
  await page.getByRole('button', { name: 'Join the waitlist' }).click();
  // Scope to the form: Next.js also renders a (hidden) route-announcer alert.
  await expect(page.locator('form').getByRole('alert')).toHaveText('Enter an email like name@example.com.');
  await expect(page.getByLabel('Email')).toHaveValue('sai@');
  await expect(page.getByLabel('Email')).toHaveAttribute('aria-invalid', 'true');
});
