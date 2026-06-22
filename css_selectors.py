#Css selectors can be selected by 
# -Tag name
# -Class name
# -id-Attribute/value

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser=playwright.chromium.launch(headless=False,slow_mo=500)
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")
  
  
  pg1 = page.locator("css=h1")
  pg1.highlight()
  pg1 = page.locator("footer")
  pg1.highlight()
   
  pg2 = page.locator("button.btn-outline-success")
  pg2.highlight()
  pg2.click()
  
  pg3 = page.locator("button#btnGroupDrop1")
  pg3.click()
  
  pg4 = page.locator("input[readonly]")
  pg4.highlight()
  pg4 = page.locator("input[value='correct value']")
  pg4.highlight()
  
  
  page.wait_for_timeout(3000) 


  browser.close() 