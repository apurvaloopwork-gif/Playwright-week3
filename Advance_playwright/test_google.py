import re 
from playwright.sync_api import expect #expect gives the assertions "Page should have this titile"

def test_google_search(page):
  page.goto("http://www.google.com",wait_until="documentloaded") #Page us automatically injected from playwright (You get a browser page )
  
  try:
    page.get_by_role("button",name="Accept all").click(timeout=5000)
    
  except:
    print("No pop up to accept")
    
    
  page.get_by_role("combobox",name = "search").fill("playwright python")
  page.keyboard.press("Enter")
  expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))