from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False,slow_mo=500)

  page=browser.new_page()
  
  page.goto('https://unsplash.com')
  pg1 = page.get_by_alt_text("a group of people sitting around a table with food")
  pg1.highlight()
  pg1 = page.get_by_alt_text("a very large object in the middle of the night sky")
  pg1.click
  
  page.wait_for_timeout(3000)
  
  browser.close()