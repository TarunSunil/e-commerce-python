import { expect, test } from '@playwright/test';

test('registers, checks out, and opens order detail and history', async ({ page }) => {
  const email = `e2e-${Date.now()}@example.com`;

  await page.goto('/register');
  await page.getByLabel('Name').fill('Browser Smoke User');
  await page.getByLabel('Email').fill(email);
  await page.getByLabel('Password').fill('correct horse');
  await page.getByRole('button', { name: 'Sign up' }).click();

  await expect(page).toHaveURL('/');
  await page.getByRole('heading', { name: 'MacBook Pro 16-inch M3 Max' }).click();
  await page.getByRole('button', { name: 'Add to Cart' }).click();
  await page.getByRole('button', { name: 'OK' }).click();

  await page.getByRole('link', { name: 'Cart' }).click();
  await expect(page.getByText('MacBook Pro 16-inch M3 Max')).toBeVisible();
  await page.getByRole('button', { name: 'Proceed to Checkout' }).click();
  await page.getByLabel('Address').fill('1 Main Street');
  await page.getByLabel('City').fill('Mumbai');
  await page.getByLabel('State').fill('MH');
  await page.getByLabel('Zip Code').fill('400001');
  await page.getByRole('button', { name: 'Place Order' }).click();

  await expect(page).toHaveURL(/\/orders\/[^/]+$/);
  await expect(page.getByText(/MacBook Pro 16-inch M3 Max/)).toBeVisible();
  await expect(page.getByText('$2499.99')).toBeVisible();

  await page.getByRole('link', { name: 'Orders' }).click();
  await expect(page).toHaveURL('/orders');
  await expect(page.getByText(/MacBook Pro 16-inch M3 Max/)).toBeVisible();
});
