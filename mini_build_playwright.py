from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)

    page = browser.new_page()

    page.goto("https://www.google.com/maps")

    search_box = page.get_by_label("Search Google Maps")
    search_box.fill("gym mumbai Andheri")
    page.keyboard.press("Enter")
    
    articles = page.locator("div[role='article']")
    articles.first.wait_for()
    # page.get_by_role("feed", name ="Search results for gym mumbai andheri").hover()
    # page.wait_for_timeout(5000)
    # page.keyboard.press("PageDown")
   
    print("Total gyms =", articles.count())
    
    # feed = page.get_by_role("feed",name = "Results for gym mumbai andheri")
    # print(feed)

    for i in range(articles.count()):
        name = articles.nth(i).get_attribute("aria-label")
        print(f"{i+1}. {name}")

    page.wait_for_timeout(5000)
    browser.close()
    
     
     