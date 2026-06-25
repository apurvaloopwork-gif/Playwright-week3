from playwright.sync_api import sync_playwright
from pages.playwright_home import PlaywrightHome

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    home = PlaywrightHome(page)
    home.open()
    home.click_get_started()
    page.wait_for_timeout(3000)

    browser.close()