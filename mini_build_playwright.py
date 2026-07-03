# from playwright.sync_api import sync_playwright
# import csv
# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False, slow_mo=500)

#     page = browser.new_page()
#     page.goto("https://www.google.com/maps")

#     search_box = page.get_by_label("Search Google Maps")
#     search_box.fill("gym mumbai Andheri")
#     page.keyboard.press("Enter")

#     articles = page.locator("div[role='article']")
#     articles.first.wait_for()
#     feed = page.locator("div[role='feed']")
#     feed.hover()
#     # page.mouse.wheel(0,2000)
#     # page.wait_for_timeout(5000)
#     # page.mouse.wheel(0,2000)
#     # page.wait_for_timeout(5000)
#     # page.mouse.wheel(0,2000)
#     # page.wait_for_timeout(5000)
#     # page.mouse.wheel(0,2000)
#     # page.wait_for_timeout(5000)
#     # page.mouse.wheel(0,2000)
#     # page.wait_for_timeout(5000)
#     # page.get_by_text("").scroll_into_view_if_needed()
#     # page.get_by_test_id("feed").evaluate("e => e.scrollTop += 100")
#     scrollable_div = page.locator("div[role='feed']")
#     scrollable_div.evaluate("el => el.scrollTop += 8000")
    
#     print("Total gyms =", articles.count())

#     with open("scraped_gym_names.csv", "w", newline="", encoding="utf-8") as f:
#         wr = csv.writer(f)
#         wr.writerow(["No", "Gym Name"])
#         for i in range(articles.count()):
#             article = articles.nth(i)
#             name = article.locator("a[aria-label]").get_attribute("aria-label")
#             print(f"{i+1}. {name}")
#             wr.writerow([i + 1, name])

#     page.wait_for_timeout(5000)
#     browser.close()

from playwright.sync_api import TimeoutError, sync_playwright
import csv


SEARCH_QUERY = "gym mumbai Andheri"
OUTPUT_FILE = "scraped_gym_names.csv"


def collect_visible_gym_names(page, names, seen):
    articles = page.locator("div[role='article']")

    for i in range(articles.count()):
        article = articles.nth(i)

        try:
            name = article.locator("a[aria-label]").first.get_attribute(
                "aria-label", timeout=1000
            )
        except TimeoutError:
            continue

        if name and name not in seen:
            seen.add(name)
            names.append(name)
            print(f"{len(names)}. {name}")


def scroll_feed_to_end(page, max_idle_scrolls=10, max_scrolls=120):
    feed = page.locator("div[role='feed']")
    feed.wait_for(timeout=15000)
    feed.hover()

    names = []
    seen = set()
    previous_total = 0
    idle_scrolls = 0

    for _ in range(max_scrolls):
        collect_visible_gym_names(page, names, seen)

        if len(names) > previous_total:
            previous_total = len(names)
            idle_scrolls = 0
        else:
            idle_scrolls += 1

        end_of_results = page.get_by_text("You've reached the end of the list.")
        if end_of_results.count() > 0 and end_of_results.first.is_visible():
            break

        if idle_scrolls >= max_idle_scrolls:
            break

        articles = page.locator("div[role='article']")
        if articles.count() > 0:
            articles.nth(articles.count() - 1).scroll_into_view_if_needed(timeout=3000)

        feed.evaluate(
            """el => {
                el.scrollBy(0, Math.max(el.clientHeight, 700));
            }"""
        )
        page.mouse.wheel(0, 2500)
        page.wait_for_timeout(2000)

    collect_visible_gym_names(page, names, seen)
    return names



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto("https://www.google.com/maps", wait_until="domcontentloaded")

    search_box = page.get_by_label("Search Google Maps")
    search_box.fill(SEARCH_QUERY)
    page.keyboard.press("Enter")

    try:
        page.locator("div[role='article']").first.wait_for(timeout=20000)
    except TimeoutError:
        browser.close()
        raise RuntimeError("No Google Maps results loaded for this search.")

    gym_names = scroll_feed_to_end(page)

    print("Total gyms =", len(gym_names))

    with open("scraped_gym_names.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["No", "Gym Name"])

        for i, name in enumerate(gym_names, start=1):
            print(f"{i}. {name}")
            writer.writerow([i, name])

    page.wait_for_timeout(5000)
    browser.close()
