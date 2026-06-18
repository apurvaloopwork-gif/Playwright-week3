from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=100)

    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    muted = page.get_by_text("With muted text")
    muted.highlight()
    
    small_button = page.get_by_text("Small button")
    small_button.highlight()
    
    fine_text=page.get_by_text("attr",exact=False)
    fine_text.highlight()
    fine_text=page.get_by_text("fine print",exact =True)
    fine_text.highlight()

    page.wait_for_timeout(3000)

    browser.close()