from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    # Login
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    # Verify Login
    title = page.inner_text(".title")
    print(title)
    assert "Products" in title
    # Add Backpack
    page.click("#add-to-cart-sauce-labs-backpack")
    # Open Cart
    page.click(".shopping_cart_link")
    # Verify Item
    item = page.inner_text(".inventory_item_name")
    print(item)
    assert "Sauce Labs Backpack" in item

    print("Test Completed Successfully!")

    browser.close()     