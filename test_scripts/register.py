from _socket import timeout
from playwright.sync_api import Playwright, sync_playwright, expect


def register(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    page.locator("//a[contains(text(),'Register')]").click()

    page.locator('id=customer.firstName').click()
    page.locator('id=customer.firstName').fill("sagar")

    page.locator("//input[@id='customer.lastName']").click()
    page.locator("//input[@id='customer.lastName']").fill("sagar")

    page.locator("//input[@id='customer.address.street']").click()
    page.locator("//input[@id='customer.address.street']").fill("abc")

    page.locator("//input[@id='customer.address.city']").click()
    page.locator("//input[@id='customer.address.city']").fill("pqr")

    page.locator("//input[@id='customer.address.state']").click()
    page.locator("//input[@id='customer.address.state']").fill("mah")

    page.locator("// input[ @ id = 'customer.address.zipCode']").click()
    page.locator("// input[ @ id = 'customer.address.zipCode']").fill("123")

    page.locator("//input[@id='customer.phoneNumber']").click()
    page.locator("//input[@id='customer.phoneNumber']").fill("12345")

    page.locator("//input[@id='customer.ssn']").click()
    page.locator("//input[@id='customer.ssn']").fill("12345")

    page.locator("//input[@id='customer.username']").click()
    page.locator("//input[@id='customer.username']").fill("sagar")

    page.locator("//input[@id='customer.password']").click()
    page.locator("//input[@id='customer.password']").fill("12345")

    page.locator("//input[@id='repeatedPassword']").click()
    page.locator("//input[@id='repeatedPassword']").fill("12345")

    page.locator("//tbody/tr[13]/td[2]/input[1]").click()


    context.close()
    browser.close()


with sync_playwright() as playwright:
    register(playwright)
