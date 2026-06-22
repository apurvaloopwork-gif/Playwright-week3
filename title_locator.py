from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False,slow_mo=500)

  page=browser.new_page()
  
  page.goto("https://bootswatch.com/default/")
  pg1=page.get_by_title("attribute")
  pg1.highlight()
  pg1=page.get_by_title("Source Title")
  pg1.highlight()

  
  page.wait_for_timeout(3000)
  
  browser.close()   