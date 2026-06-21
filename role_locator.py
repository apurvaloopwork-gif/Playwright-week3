from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=100)

    page = browser.new_page()

    page.goto("https://playwright.dev/python")

    btn = page.get_by_role("link",name="GET STARTED")

    btn.highlight()
    btn.click()

    page.wait_for_timeout(3000)

    browser.close()