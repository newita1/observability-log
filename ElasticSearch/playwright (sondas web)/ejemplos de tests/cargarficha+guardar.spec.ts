import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {

  await test.step('01. Load Webpage', async () =>{
    await page.goto('http://url/Account/Login');
  });

  await test.step('02. Login', async () =>{
    await page.getByLabel('Usuario').fill('');
    await page.getByLabel('Contraseña').fill('');
    await page.locator('input[value="Log in"]').click();
  });

  await test.step('03. Load HomePage', async () =>{
    await page.locator('span', {hasText: 'CASINO'}).click();
    await page.locator('#ClienteRecepcion_TextoBusqueda').fill('');
    await page.locator('#ClienteRecepcion_TextoBusqueda').press('Enter');

  });

  await test.step('04. Save File', async () =>{
    await expect(page.locator('#page-wrapper div').filter({ hasText: 'Datos del Cliente Nombre' }).nth(1)).toBeVisible();
    await page.locator('xpath=').click();
    await expect(page.locator('.ibox-title > .ibox-tools')).toBeVisible();
  });

  
});


