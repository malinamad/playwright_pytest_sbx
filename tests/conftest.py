import pytest
from playwright.sync_api import sync_playwright
from pages import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        '--environment',
        action='store',
        default='local',
        help='Environment where the tests should run.'
    )


@pytest.fixture(scope="module")
def set_environment(request):
    yield request.config.getoption('--environment')


@pytest.fixture(scope="module", name='browser')
def playwright_browser(set_environment):
    page_envs = {'local', 'QA', 'UAT', 'PROD', 'test'}
    if set_environment in page_envs:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            yield browser


@pytest.fixture()
def login_page(browser):
    page = browser.new_context().new_page()
    login_page = LoginPage.LoginPage(page)
    yield login_page
    page.close()


@pytest.fixture(scope="module", name='credentials')
def set_up_credentials(set_environment):
    if set_environment == 'local':
        username = 'standard_user'
        password = 'secret_sauce'
        yield username, password
    elif set_environment == 'QA':
        qa_username = 'standard_user'
        qa_password = 'secret_sauce'
        yield qa_username, qa_password
    elif set_environment == 'UAT':
        uat_username = 'standard_user'
        uat_password = 'secret_sauce'
        yield uat_username, uat_password
    elif set_environment == 'PROD':
        prod_username = 'standard_user'
        prod_password = 'secret_sauce'
        yield prod_username, prod_password
    else:
        raise NameError(f'Unknown {set_environment} environment.')


@pytest.fixture(scope="class")
def login_page(browser):
    page = browser.new_context().new_page()
    login_page = LoginPage.LoginPage(page)
    yield login_page
