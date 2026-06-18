from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    page.locator("nav.bg-dark a.nav-link.active").highlight()

    page.wait_for_timeout(5000)

    browser.close()