from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False,slow_mo=5000)
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")
  page.get_by_role("button",name="Block button").highlight()
  page.wait_for_timeout(2000)
  
  button = page.get_by_role("button",name="Block button").first
  page.wait_for_timeout(2000)
  
  page.locator("footer").highlight()
  page.wait_for_timeout(2000)
  
  button.click()
  button.dbclick()
  button.dbclick(delay=500)
  
  button.click(button="right")
  button.click(modifiers=["shift"])
  button.click(modifiers=["shift","Meta"])
  outline_button=page.locator("button.btn=outline-primary")
  outline_button.hover()
browser.close()