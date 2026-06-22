from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless = False,slow_mo=500)
  page = browser.new_page()
  
  page.goto("https://www.google.com/maps")
  page.wait_for_timeout(2000)
  
  serach_box = page.get_by_label("Search Google Maps")
  serach_box.fill("gym mumbai Andheri")
  page.keyboard.press("Enter")
  page.wait_for_timeout(2000)
  
  
  browser.close() 
