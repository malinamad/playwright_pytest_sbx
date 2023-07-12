from playwright.sync_api import sync_playwright

username = 'standard_user'
password = 'secret_sauce'

def test_automate_website(browser, login_page):
    login_page.open_login_page()
    login_page.login_to_the_environment(username, password)
    browser.close()
