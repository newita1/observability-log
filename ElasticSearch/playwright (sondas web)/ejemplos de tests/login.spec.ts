import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await test.step('01. Load Webpage', async () =>{
    await page.goto('http://url/Account/Login');
  });

  await test.step('02. Login', async () =>{
    await page.getByLabel('Usuario').click();
    await page.getByLabel('Usuario').fill('');
    await page.getByLabel('Contraseña').click();
    await page.getByLabel('Contraseña').fill('');
    await page.locator('input[value="Log in"]').click();
  });

  await test.step('03. Load HomePage', async () =>{
    await expect(page.getByText('Seleccione el centro al que desea conectar.')).toBeVisible();
  });
  
  
});