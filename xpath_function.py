from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)

    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    page.locator("//h2[text()='Heading 1']").highlight()
    page.wait_for_timeout(2000)

    page.locator("//h1[contains(text(),'Head')]").highlight()
    page.wait_for_timeout(2000)

    page.locator("//button[contains(@class,'btn-outline-primary')]").highlight()
    page.wait_for_timeout(2000)
    
    page.locator("//input[contains(@value,'correct')]").highlight()
    page.wait_for_timeout(2000)

    browser.close()