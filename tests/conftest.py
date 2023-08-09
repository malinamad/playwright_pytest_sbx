import pytest
from pages import LoginPage
from playwright.sync_api import sync_playwright, expect
# from utilities.utilities import test_utility, run_on


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


@pytest.fixture(scope="module", name='credentials')
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


@pytest.fixture(scope="class")
def login_page(browser):
    page = browser.new_context().new_page()
    login_page = LoginPage.LoginPage(page)
    yield login_page