import pytest
from pages import LoginPage
from playwright_pytest_sbx.utilities import utilities


def test_successful_login_to_the_environment(browser, login_page, credentials) -> None:
    username, password = credentials
    login_page.open_login_page()
    login_page.login_to_the_environment(username, password)
    login_page.main_page_is_present()


def test_incorrect_password_login(browser, login_page, credentials) -> None:
    username, password = credentials
    login_page.open_login_page()
    login_page.login_to_the_environment(username, 'test')
    login_page.unsuccessful_login_error_message_is_present()
    utilities.take_screenshot(login_page.page, 'unsuccessful_login_incorrect_password')


def test_incorrect_username_login(browser, login_page, credentials) -> None:
    username, password = credentials
    login_page.open_login_page()
    login_page.login_to_the_environment('test', password)
    login_page.unsuccessful_login_error_message_is_present()
    utilities.take_screenshot(login_page.page, 'unsuccessful_login_incorrect_username')
