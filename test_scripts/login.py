from playwright.sync_api import Playwright, sync_playwright, expect


def login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://parabank.parasoft.com/parabank/index.htm")

    page.locator("//input[@name='username']").click()
    page.locator("//input[@name='username']").fill("sss")

    page.locator("//input[@name='password']").click()
    page.locator("//input[@name='password']").fill("123")

    page.locator("//body/div[@id='mainPanel']/div[@id='bodyPanel']/div[@id='leftPanel']"
                 "/div[@id='loginPanel']/form[1]/div[3]/input[1]").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    login(playwright)
