from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False,slow_mo=500)
  
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")
  
  select = page.get_by_label("Example select")
  select.select_option("4")
  page.wait_for_timeout(3000)
  select.select_option("2")
  page.wait_for_timeout(3000)
  select.select_option("5")
  page.wait_for_timeout(3000)
  select.select_option("10")#If I enter Option which is not in it then it will wait for time out and will give error
  page.wait_for_timeout(3000)
  
  multi_select = page.get_by_label("Example multiple select")
  multi_select.select_option(["1","2","3","5"])
browser.close()  