
from playwright.sync_api import Playwright, sync_playwright, expect


def products_page_checkbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    page.locator("//body/div[@id='mainPanel']/div[@id='headerPanel']/ul[1]/li[4]/a[1]").click()

    page.locator("// a[contains(text(), 'Request a Demo')]").click()

    page.locator("//label[contains(text(),'API Security Testing')]").click()

    page.locator("//label[contains(text(),'API Testing')]").click()

    page.locator("//label[contains(text(),'Continuous Testing')]").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    products_page_checkbox(playwright)
