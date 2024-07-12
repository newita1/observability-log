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

  })
  await test.step('04. Send Entree', async () =>{
    await page.locator('a').filter({ hasText: 'Captacion [001]' }).click();
    await page.locator('li').filter({ hasText: 'Captacion [001]' }).click();
    await page.locator('xpath=//').click();
    await page.locator('xpath=//').click();

    const isVisible = await page.locator('text=Cliente en sala').isVisible();
    if (isVisible) {
        await page.locator('button:has-text("Aceptar")').click();
    }
    
  });
  await test.step('06. Verify Entree', async () =>{
    await page.locator('.refreshEntradas').click();
    await expect(page.getByRole('gridcell', { name: '' })).toBeVisible();
  });
});