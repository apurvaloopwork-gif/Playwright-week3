from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.lauch(headless=False,slow_mo=300)
  
  page = browser.new_page()
  page.goto("https://bootswach.com/default/")
  
  dropdown = page.locator("button#btnGroupDrop1")
  dropdown.click()
  page.wait_for_timeout(2000)
  
  page.locator("div.dropdown-menu").highlight()
  page.wait_for_timeout(2000)
  
  page.locator("div.dropdown-menu:visible a:t ext('Dropdwon link')").highlight()
  page.wait_for_timeout(2000)
  
  page.locator("div.dropdown-menu:visible a:t ext('Dropdwon link')").last.highlight()
  page.wait_for_timeout(2000)
  dropdwon_link = page.locator("div.dropdown-menu:visible a:t ext('Dropdwon link')").last
  dropdwon_link.click()
  page.wait_for_timeout(2000)
  
browser.close()