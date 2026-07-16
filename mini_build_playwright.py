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
import re
import urllib.parse


SEARCH_QUERY = "gym mumbai Andheri"
OUTPUT_FILE = "scraped_gym_names.csv"


def dismiss_google_popups(page):
    for label in ("Accept all", "Reject all", "I agree", "Accept"):
        try:
            button = page.get_by_role("button", name=label)
            if button.count() > 0 and button.first.is_visible():
                button.first.click(timeout=3000)
                page.wait_for_timeout(1500)
                return
        except TimeoutError:
            continue


def wait_for_results(page, timeout_ms=45000):
    try:
        page.locator("div[role='feed']").first.wait_for(
            state="visible", timeout=timeout_ms
        )
        return True
    except TimeoutError:
        pass

    try:
        page.locator("div[role='article']").first.wait_for(
            state="visible", timeout=5000
        )
        return True
    except TimeoutError:
        return False


def open_search_results(page, query):
    dismiss_google_popups(page)

    search_url = (
        "https://www.google.com/maps/search/"
        + urllib.parse.quote(query)
    )
    page.goto(search_url, wait_until="load", timeout=60000)
    page.wait_for_timeout(2000)
    dismiss_google_popups(page)

    if wait_for_results(page):
        return

    page.goto("https://www.google.com/maps", wait_until="load", timeout=60000)
    page.wait_for_timeout(2000)
    dismiss_google_popups(page)

    search_box = page.locator("#searchboxinput")
    search_box.wait_for(state="visible", timeout=15000)
    search_box.fill(query)
    search_box.press("Enter")
    page.wait_for_timeout(3000)

    if wait_for_results(page):
        return

    page.screenshot(path="maps_search_error.png")
    raise RuntimeError(
        "No Google Maps results loaded for this search. "
        "A screenshot was saved as maps_search_error.png. "
        "If you see a captcha or login screen in the browser, solve it and run again."
    )


def extract_phone_from_panel(page):
    try:
        phone_btn = page.locator('button[data-item-id="phone"]')
        if phone_btn.count() > 0:
            text = phone_btn.first.inner_text(timeout=3000).strip()
            if text:
                return text
    except TimeoutError:
        pass

    try:
        tel_link = page.locator('a[href^="tel:"]').first
        if tel_link.count() > 0:
            href = tel_link.get_attribute("href") or ""
            if href:
                return href.replace("tel:", "").strip()
    except TimeoutError:
        pass

    try:
        copy_phone = page.locator('[data-tooltip="Copy phone number"]').first
        if copy_phone.count() > 0:
            aria = copy_phone.get_attribute("aria-label") or ""
            match = re.search(r"Phone:\s*(.+)", aria, re.IGNORECASE)
            if match:
                return match.group(1).strip()
    except TimeoutError:
        pass

    return ""


def return_to_results_feed(page):
    feed = page.locator("div[role='feed']")
    if feed.count() > 0 and feed.first.is_visible():
        return

    back_btn = page.locator('button[aria-label="Back"]')
    try:
        if back_btn.count() > 0 and back_btn.first.is_visible():
            back_btn.first.click(timeout=3000)
            feed.first.wait_for(state="visible", timeout=8000)
            return
    except TimeoutError:
        pass

    try:
        page.keyboard.press("Escape")
        feed.first.wait_for(state="visible", timeout=5000)
    except TimeoutError:
        pass


def collect_visible_gyms(page, gyms, seen):
    articles = page.locator("div[role='article']")

    for i in range(articles.count()):
        article = articles.nth(i)

        try:
            link = article.locator("a[aria-label]").first
            name = link.get_attribute("aria-label", timeout=1000)
        except TimeoutError:
            continue

        if not name or name in seen:
            continue

        seen.add(name)
        phone = ""

        try:
            link.scroll_into_view_if_needed(timeout=3000)
            link.click(timeout=5000)
            page.locator("h1").first.wait_for(state="visible", timeout=8000)
            phone = extract_phone_from_panel(page)
        except TimeoutError:
            pass
        except Exception as exc:
            print(f"  Skipped phone for '{name}': {exc}")
        finally:
            return_to_results_feed(page)

        gyms.append({"name": name, "phone": phone})
        print(f"{len(gyms)}. {name} | {phone or 'N/A'}")


def scroll_feed_to_end(page, max_idle_scrolls=10, max_scrolls=120):
    feed = page.locator("div[role='feed']")
    feed.wait_for(timeout=15000)
    feed.hover()

    gyms = []
    seen = set()
    previous_total = 0
    idle_scrolls = 0

    for _ in range(max_scrolls):
        collect_visible_gyms(page, gyms, seen)

        if len(gyms) > previous_total:
            previous_total = len(gyms)
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

    collect_visible_gyms(page, gyms, seen)
    return gyms



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context(
        viewport={"width": 1280, "height": 900},
        locale="en-US",
    )
    page = context.new_page()

    open_search_results(page, SEARCH_QUERY)

    gyms = scroll_feed_to_end(page)

    print("Total gyms =", len(gyms))

    try:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["No", "Gym Name", "Contact Number"])

            for i, gym in enumerate(gyms, start=1):
                writer.writerow([i, gym["name"], gym["phone"]])
    except PermissionError:
        raise PermissionError(
            f"Could not write to '{OUTPUT_FILE}'. Close the file if it is open in Excel, then run again."
        )

    page.wait_for_timeout(5000)
    context.close()
    browser.close()
