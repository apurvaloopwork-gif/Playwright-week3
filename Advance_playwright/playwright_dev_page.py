from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://playwright.dev")
    page.click("text=Get started")
    page.wait_for_timeout(3000)
    browser.close()
