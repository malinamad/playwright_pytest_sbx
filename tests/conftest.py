import pytest
from playwright.sync_api import sync_playwright, expect
from utilities.utilities import test_utility, run_on
from pages import LoginPage


@pytest.fixture(name='browser')
def playwright_browser():
    print(run_on)
    if run_on == 'local':
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            yield browser


@pytest.fixture()
def login_page(browser):
    page = browser.new_context().new_page()
    login_page = LoginPage.LoginPage(page)
    yield login_page


@pytest.fixture(name='credentials')
def set_up_env_credentials():
    if run_on == 'local':
        qa_username = 'standard_user'
        qa_password = 'secret_sauce'
        yield qa_username, qa_password

# @pytest.fixture
# def home_page(browser):
#     page = browser.new_context().new_page()
#     home_page = homepage.HomePage(page)
#     yield home_page
#
#
# @pytest.fixture
# def product_page(browser):
#     page = browser.new_context().new_page()
#     product_page = productpage.ProductPage(page)
#     yield product_page

# username = 'standard_user'
# password = 'secret_sauce'
#
#
# def test_automate_website(browser, login_page):
#     login_page.open_login_page()
#     login_page.login_to_the_environment(username, password)
#     browser.close()
