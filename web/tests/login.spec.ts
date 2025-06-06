import { test, expect } from '@playwright/test';

test.describe('Login Page', () => {
  test('should login successfully with valid credentials', async ({ page }) => {
    await page.goto('http://localhost:3000/login'); // Update URL as needed

    await page.fill('[data-testid="username_input"]', 'testuser');
    await page.fill('[data-testid="password_input"]', 'password123');
    await page.click('[data-testid="login_button"]');

    // Replace with an assertion relevant to your app, e.g., check for home screen
    await expect(page).toHaveURL(/.*dashboard/);
  });

  test('should show error message with invalid credentials', async ({ page }) => {
    await page.goto('http://localhost:3000/login'); // Update URL as needed

    await page.fill('[data-testid="username_input"]', 'wronguser');
    await page.fill('[data-testid="password_input"]', 'wrongpass');
    await page.click('[data-testid="login_button"]');

    await expect(page.locator('[data-testid="error_message"]')).toHaveText('Invalid credentials');
  });
});