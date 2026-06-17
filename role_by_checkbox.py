from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=100)

    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    checkbox = page.get_by_role(
        "checkbox",
        name="Default checkbox"
    )

    checkbox.highlight()
    checkbox.check()

    page.wait_for_timeout(3000)

    browser.close()