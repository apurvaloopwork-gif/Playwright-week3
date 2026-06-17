from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=100)

    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    email_input = page.get_by_label("Email address")
    email_input.highlight()

    password_input = page.get_by_label("Password")
    password_input.highlight()

    page.wait_for_timeout(3000)

    browser.close()