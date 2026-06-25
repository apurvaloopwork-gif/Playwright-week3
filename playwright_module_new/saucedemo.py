from playwright.sync_api import sync_playwright

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False, slow_mo=500)
   page = browser.new_page()
   page.goto("https://www.saucedemo.com")
   page.fill("#user-name", "standard_user")
   page.fill("#password", "secret_sauce")
   page.click("#login-button")
   text = page.inner_text(".title")
   assert "Products" in text
   browser.close()