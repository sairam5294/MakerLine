import { expect, test } from '@playwright/test';

test('home → sign in with keyboard only, and an empty email shows an announced error', async ({
  page,
}) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await expect(page.getByRole('heading', { name: 'Sign in' })).toBeVisible();

  // Submit without typing: error appears in an alert (read out by screen readers).
  await page.getByRole('button', { name: 'Send code' }).click();
  await expect(page.getByRole('alert')).toHaveText('Enter your email address.');

  // Keyboard: the email field can be focused and typed into.
  await page.getByLabel('Email').focus();
  await page.keyboard.type('not-an-email');
  await page.keyboard.press('Enter');
  await expect(page.getByRole('alert')).toHaveText('Enter an email like name@example.com.');
});
