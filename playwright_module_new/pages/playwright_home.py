class PlaywrightHome:

    def __init__(self, page):
        self.page = page

        # Locators
        self.get_started_button = page.locator("text=Get started")

    def open(self):
        self.page.goto("https://playwright.dev")

    def click_get_started(self):
        self.get_started_button.click()
        
        