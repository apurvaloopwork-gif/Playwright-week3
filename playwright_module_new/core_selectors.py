# #id
# .class
# tag - element type 
# [attr=val] - attritubes

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    #  ID Selector (#)  
    page.locator("#navbar").highlight()
    page.wait_for_timeout(2000)
    #Class Selector (.)   
    page.locator(".navbar").highlight()
    page.wait_for_timeout(2000)   
    # Tag Selector  
    page.locator("h1").highlight()
    page.wait_for_timeout(2000)  
    #Attribute Selector
    page.locator("[type='text']").first.highlight()
    page.wait_for_timeout(2000)

    browser.close()

