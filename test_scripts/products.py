
from playwright.sync_api import Playwright, sync_playwright, expect


def products(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    page.locator("//body/div[@id='mainPanel']/div[@id='headerPanel']/ul[1]/li[4]/a[1]").click()

    page.locator("// a[contains(text(), 'Request a Demo')]").click()

    page.locator("//body/section[2]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/a[1]").click()

    page.locator("//input[@id='email-ac031725-1541-4bcb-a4b1-baf748fba09b']").click()
    page.locator("//input[@id='email-ac031725-1541-4bcb-a4b1-baf748fba09b']").fill("abc@parasoft.com")

    page.locator("//input[@id='firstname-ac031725-1541-4bcb-a4b1-baf748fba09b']").click()
    page.locator("//input[@id='firstname-ac031725-1541-4bcb-a4b1-baf748fba09b']").fill("sagar")

    page.locator("#lastname-ac031725-1541-4bcb-a4b1-baf748fba09b").click()
    page.locator("#lastname-ac031725-1541-4bcb-a4b1-baf748fba09b").fill("sagar")

    page.locator("#company-ac031725-1541-4bcb-a4b1-baf748fba09b").click()
    page.locator("#company-ac031725-1541-4bcb-a4b1-baf748fba09b").fill("parasoft Tech")

    page.locator("#jobtitle-ac031725-1541-4bcb-a4b1-baf748fba09b").click()
    page.locator("#jobtitle-ac031725-1541-4bcb-a4b1-baf748fba09b").fill("Tester")

    page.locator("#phone-ac031725-1541-4bcb-a4b1-baf748fba09b").click()
    page.locator("#phone-ac031725-1541-4bcb-a4b1-baf748fba09b").fill("1234567890")

    page.locator("#country-ac031725-1541-4bcb-a4b1-baf748fba09b").select_option("India")
    page.locator("// body / section[1] / div[1] / div[1] / div[2] / div[1] / div[1] / "
                 "div[1] / form[1] / div[15] / div[2] / input[1]").click()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    products(playwright)
