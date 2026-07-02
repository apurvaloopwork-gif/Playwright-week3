from playwright.sync_api import sync_playwright
import csv
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    page = browser.new_page()
    page.goto("https://www.google.com/maps")

    search_box = page.get_by_label("Search Google Maps")
    search_box.fill("gym mumbai Andheri")
    page.keyboard.press("Enter")

    articles = page.locator("div[role='article']")
    articles.first.wait_for()
    feed = page.locator("div[role='feed']")
    feed.hover()
    # page.mouse.wheel(0,2000)
    # page.wait_for_timeout(5000)
    # page.mouse.wheel(0,2000)
    # page.wait_for_timeout(5000)
    # page.mouse.wheel(0,2000)
    # page.wait_for_timeout(5000)
    # page.mouse.wheel(0,2000)
    # page.wait_for_timeout(5000)
    # page.mouse.wheel(0,2000)
    # page.wait_for_timeout(5000)
    # page.get_by_text("").scroll_into_view_if_needed()
    # page.get_by_test_id("feed").evaluate("e => e.scrollTop += 100")
    scrollable_div = page.locator("div[role='feed']")
    scrollable_div.evaluate("el => el.scrollTop += 8000")
    print("Total gyms =", articles.count())

    with open("scraped_gym_names.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["No", "Gym Name"])

        for i in range(articles.count()):
            article = articles.nth(i)
            name = article.locator("a[aria-label]").get_attribute("aria-label")
            print(f"{i+1}. {name}")
            wr.writerow([i + 1, name])

    page.wait_for_timeout(5000)
    browser.close()