from _socket import timeout
from playwright.sync_api import Playwright, sync_playwright, expect


def customer_care(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//a[contains(text(),'contact')]").click()
    page.locator('id=name').click()
    page.locator('id=name').fill("sagar")

    page.locator('id=email').click()
    page.locator('id=email').fill("abc@gmail.com")

    page.locator('id=phone').click()
    page.locator('id=phone').fill("1234567890")

    page.locator('id=message').click()
    page.locator('id=message').fill("test_scripts")

    page.locator("//tbody/tr[5]/td[2]/input[1]").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    customer_care(playwright)
