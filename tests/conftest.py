import pytest
from playwright.sync_api import sync_playwright, expect
from pages import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        '--environment',
        action='store',
        default='local',
        help='Environment where the tests should run.'
    )


@pytest.fixture
def set_environment(request):
    yield request.config.getoption('--environment')


@pytest.fixture(name='browser')
def playwright_browser(set_environment):
    page_envs = {'local', 'QA', 'UAT', 'PROD', 'test'}
    # print(set_environment)
    if set_environment in page_envs:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            yield browser


@pytest.fixture()
def login_page(browser):
    page = browser.new_context().new_page()
    login_page = LoginPage.LoginPage(page)
    yield login_page


@pytest.fixture(name='credentials')
def set_up_credentials(set_environment):
    if set_environment == 'local':
        qa_username = 'standard_user'
        qa_password = 'secret_sauce'
        yield qa_username, qa_password
    elif set_environment == 'QA':
        qa_username = 'standard_user'
        qa_password = 'secret_sauce'
        yield qa_username, qa_password
    elif set_environment == 'UAT':
        qa_username = 'standard_user'
        qa_password = 'secret_sauce'
        yield qa_username, qa_password
    elif set_environment == 'PROD':
        qa_username = 'standard_user'
        qa_password = 'secret_sauce'
        yield qa_username, qa_password
    else:
        raise Exception(f'Unknown {set_environment} environment.')

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
