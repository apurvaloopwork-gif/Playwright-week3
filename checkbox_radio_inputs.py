from playwright.sync_api import sync_playwright



with sync_playwright() as playwright:
  browser=playwright.chromium.launch(headless=False,slow_mo=500)
  
  page=browser.new_page()
  page.goto("https://bootswatch.com/default/") 
  
  radio_option2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
  
  radio_option1 = page.get_by_label("Option is this and that-be sure to include why it's great")
  radio_option1.check()
  
  checkbox = page.get_by_label("Default check box")
  checkbox.check()#check method will check only if it's not check 
  checkbox.is_checked() #To check the checkbox
  
  checkbox.uncheck()#To uncheck the checkbox
  checkbox.set_checked(True)
  
  checkbox.click() #checks it
  checkbox.click() #unchecks it just like a normal click and clicking it again
  
  switch = page.get_by_label("Checked switch checkbox input")
  
  switch.uncheck()
  switch.check()
browser.close()