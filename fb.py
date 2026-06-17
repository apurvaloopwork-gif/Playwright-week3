# .\venv\Scripts\activate
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  #Lauch bowser
  browser = playwright.chromium.launch(headless=False,slow_mo=1000)
  #Create a new page
  page=browser.new_page()
  #visit the playwright website
  page.goto("https://www.facebook.com/")
  
  
  #Locate a link element with "docs" text
  docs_button=page.get_by_label("Email address or mobile number").fill("hometvs1982@gmail.com")
  docs_button=page.get_by_label("Password").fill("Hometvs@1982")
  
  docs_button=page.get_by_role('button',name="Log in")
  docs_button.click()
  #To get the page URL
  print("Docs:",page.url)
  
  time.sleep(20)
  browser.close()
