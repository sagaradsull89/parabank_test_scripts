from _socket import timeout
from playwright.sync_api import Playwright, sync_playwright, expect


def forgot_login_info(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//a[contains(text(),'Forgot login info?')]").click()
    page.locator('id=firstName').click()
    page.locator('id=firstName').fill("sagar")

    page.locator('id=lastName').click()
    page.locator('id=lastName').fill("sagar")

    page.locator('id=address.street').click()
    page.locator('id=address.street').fill("abc")

    page.locator('id=address.city').click()
    page.locator('id=address.city').fill("pqr")

    page.locator('id=address.state').click()
    page.locator('id=address.state').fill("mah")

    page.locator('id=address.zipCode').click()
    page.locator('id=address.zipCode').fill("123")

    page.locator('id=ssn').click()
    page.locator('id=ssn').fill("12345")

    page.locator("//tbody/tr[8]/td[2]/input[1]").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    forgot_login_info(playwright)
