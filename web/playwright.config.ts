import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  projects: [
    // ...existing projects...
    {
      name: 'Mobile Safari (iPhone 16)',
      use: {
        ...devices['iPhone 16'],
      },
    },
  ],
  // ...existing config...
});