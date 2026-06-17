# .\venv\Scripts\activate
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  #Lauch bowser
  browser = playwright.chromium.launch(headless=False,slow_mo=500)
  #Create a new page
  page=browser.new_page()
  #visit the playwright website
  page.goto("https://playwright.dev/python")
  
  
  #Locate a link element with "docs" text
  docs_button=page.get_by_role('Link',name="Docs")
  docs_button.click() 
  #To get the page URL
  print("Docs:",page.url)
  browser.close()
