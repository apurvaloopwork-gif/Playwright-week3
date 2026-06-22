from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless = False,slow_mo=500)
  
  page=browser.new_page()
  page.goto("https://bootswatch.com/default/")
  
  file_input = page.get_by_label("Default file input example")
  
  file_input.set_input_files("file.txt")
  page.wait_for_timeout(2000)
  
  with page.expect_file_chooser() as fc_info:
    file_input.click()
    
  file_chooser = fc_info.value
  file_chooser.set_files("get_by_text.py")
  browser.close()