from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    page.wait_for_timeout(2000)

    # Highlight first h1
    page.locator("xpath=//h1").highlight()
    page.wait_for_timeout(2000)

    # Highlight h1 with id='navbars'
    page.locator("xpath=//h1[@id='navbars']").highlight()
    page.wait_for_timeout(2000)

    # Highlight readonly input
    page.locator("//input[@readonly]").highlight()
    page.wait_for_timeout(2000)

    # Highlight input having value='wrong value'
    page.locator("//input[@value='wrong value']").highlight()
    page.wait_for_timeout(5000)

    browser.close()