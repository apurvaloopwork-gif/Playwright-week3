from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)

    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")

    page.get_by_role("button", name="Submit").click()

    page.wait_for_load_state("networkidle")#waits till the page loads

    success_text = page.locator("h1").inner_text()

    if success_text == "Logged In Successfully":
        print("Completed Successfully")
    else:
        print("Failed")

    page.wait_for_timeout(5000)

    browser.close()