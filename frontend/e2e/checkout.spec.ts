import { expect, test } from '@playwright/test';

test('registers, checks out, and opens order detail and history', async ({ page }) => {
  const email = `e2e-${Date.now()}@example.com`;
  const failedResponses: string[] = [];
  const failedRequests: string[] = [];
  const consoleErrors: string[] = [];

  page.on('response', async (response) => {
    if (response.status() < 400) return;
    let bodySnippet = '';
    try {
      bodySnippet = (await response.text()).slice(0, 500);
    } catch {
      bodySnippet = '<unavailable>';
    }
    failedResponses.push(
      `[${response.status()}] ${response.request().method()} ${response.url()} body=${bodySnippet}`
    );
  });

  page.on('requestfailed', (request) => {
    failedRequests.push(
      `${request.method()} ${request.url()} error=${request.failure()?.errorText ?? 'unknown'}`
    );
  });

  page.on('console', (message) => {
    if (message.type() === 'error') {
      consoleErrors.push(message.text());
    }
  });

  await page.goto('/register');
  await page.getByLabel('Name').fill('Browser Smoke User');
  await page.getByLabel('Email').fill(email);
  await page.getByLabel('Password').fill('correct horse');
  const registerResponsePromise = page
    .waitForResponse(
      (response) =>
        response.request().method() === 'POST' && response.url().includes('/api/auth/register'),
      { timeout: 10000 }
    )
    .catch(() => null);
  await page.getByRole('button', { name: 'Sign up' }).click();
  const registerResponse = await registerResponsePromise;

  try {
    await expect(page).toHaveURL('/');
  } catch (error) {
    if (registerResponse) {
      let responseBody = '<unavailable>';
      try {
        responseBody = (await registerResponse.text()).slice(0, 500);
      } catch {
        responseBody = '<unavailable>';
      }
      console.log(
        `[register-response] status=${registerResponse.status()} url=${registerResponse.url()} body=${responseBody}`
      );
    } else {
      console.log('[register-response] no register response was captured');
    }

    if (failedResponses.length) {
      console.log('[failed-responses]', failedResponses.join('\n'));
    }
    if (failedRequests.length) {
      console.log('[failed-requests]', failedRequests.join('\n'));
    }
    if (consoleErrors.length) {
      console.log('[console-errors]', consoleErrors.join('\n'));
    }
    throw error;
  }

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
