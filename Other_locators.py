from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser=playwright.chromium.launch(headless=False,slow_mo=5000)
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")
  
  page.get_by_role("button",name="primary").highlight()
  page.wait_for_timeout(2000)
  page.get_by_role("button",name="primary").locator("nth=1").highlighy()
  page.wait_for_timeout(2000)
  
  page.locator("button").locator("nth=18").highlight()
  page.wait_for_timeout(2000)
  
  page.get_by_label("Email address").highlight()
  page.wait_for_timeout(2000)
  
  page.get_by_label("Email address").locator("..").highlight()
  page.wait_for_timeout(2000)
  
  page.locator("id=btnGroupDrop1").highlight()
  page.wait_for_timeout(2000)
  
  page.locator("div.dropdown-menu").locator("visible=true").highlight()
  page.wait_for_timeout(2000)
  
  page.get_by_role("heading").highlight()
  page.wait_for_timeout(2000)
  page.get_by_role("heading").filter(has_text="Heading").highlight()
  page.wait_for_timeout(2000)
  
  page.locator("div.form-group").filter(has=page.get_by_label("password")).highlight() 
  page.wait_for_timeout(2000)
  browser.close()