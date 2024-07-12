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
    await page.locator('span', {hasText: 'CASINO'}).click();
    await page.locator('xpath=//').click();

  });

  await test.step('04. Get User', async () =>{
    await page.getByLabel('Cliente', { exact: true }).fill('PEPE VIYUELA');
    await page.getByText('Hombre').click();
    await page.locator('button').filter({ hasText: 'Buscar' }).click();
    await expect(page.locator('#DataTables_Table_0').getByText('')).toBeVisible();
  });

  
});