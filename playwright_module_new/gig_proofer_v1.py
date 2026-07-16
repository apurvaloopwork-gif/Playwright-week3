from playwright.sync_api import sync_playwright

EMAIL = ""
PASSWORD = "."

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.fiverr.com/login")

    page.get_by_label("Email").fill(EMAIL)
    page.get_by_label("Password").fill(PASSWORD)

    
    page.get_by_role("button", name="Sign In").click()

    print("Please solve the CAPTCHA manually.")

    input("Press Enter after you're logged in...")

    page.goto("https://www.fiverr.com/users/me/earnings")

    input("Press Enter to close...")

    browser.close()