from playwright.sync_api import sync_playwright



with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False,slow_mo=500)

  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")
  page.get_by_label("Email address").highlight()
  
  page.locator("footer").highlight()
  
  input = page.get_by_placeholder("Enter email")
  input.fill("me@that.site")
  input.clear()
  input.type("me@thst.site")
  input.type("me@thst.site",delay=200)
  valid_input=page.get_by_label("valid input").first
  valid_input.input_value()
 
  browser.close()    