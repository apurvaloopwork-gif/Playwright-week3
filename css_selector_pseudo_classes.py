from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    
    page.goto("https://bootswatch.com/default/")

    
    page.wait_for_timeout(2000)

   
    page.locator("h1").highlight()
    page.wait_for_timeout(2000)

    
    page.locator("h1:text('Nav')").highlight()
    page.wait_for_timeout(2000)

    
    #  Exact Text Match
    
    page.locator("h1:text-is('Navbars')").highlight()
    page.wait_for_timeout(2000)

   
    #  Visible Dropdown Menu
    
    page.locator("div.dropdown-menu:visible").highlight()
    page.wait_for_timeout(2000)

   
    #  Fourth Primary Button
    
    page.locator(
        ":nth-match(button.btn-primary, 4)").highlight()
    page.wait_for_timeout(2000)

  
    #  First Button Having Text
    
    page.locator(
        ":nth-match(button:text('Primary'), 1)").highlight()
    page.wait_for_timeout(2000)

    print("All selectors executed successfully!")

    page.wait_for_timeout(5000)

    browser.close()