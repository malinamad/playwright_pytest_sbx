from playwright.sync_api import sync_playwright
from configs.config import URL
from pages import InstancePage

def automate_website():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        main_page = InstancePage(page)
        main_page.navigate_to_website(URL)
        main_page.take_screenshot('screenshots/screenshot.jpg')

        context.close()


if __name__ == '__main__':
    automate_website()
