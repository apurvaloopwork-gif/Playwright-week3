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
    print("Total gyms =", articles.count())

    for i in range(articles.count()):
        name = articles.nth(i).get_attribute("aria-label")
        print(f"{i+1}. {name}")

    page.wait_for_timeout(5000)
    browser.close()
    
    