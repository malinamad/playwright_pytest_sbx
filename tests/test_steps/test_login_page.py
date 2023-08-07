import pytest
from pages import LoginPage

from pytest_bdd import scenarios, given, when, then


# scenarios("../features/login_page.feature")

@pytest.fixture()
def context():
    return {
        "username": None,
        "password": None
    }


@given("I'm A Standard User")
def test_standard_user(credentials, context):
    username, password = credentials
    context["username"] = username
    context["password"] = password


@when("I Am On The Login Page")
def test_user_is_on_login_page(browser, page, context):
    page = browser.new_context().new_page()
    login_page = LoginPage.LoginPage(page)
    login_page.open_login_page()
    login_page.login_to_the_environment(
        "test", "test"
    )


@then("I Should Be Able To Login With My Credentials")
def test_products_page_is_displayed(page):
    login_page.unsuccessful_login_error_message_is_present()
