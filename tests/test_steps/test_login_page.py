import pytest
from pages import LoginPage
from pytest_bdd import scenarios, given, when, then


# scenarios("../features/login_page.feature")


@pytest.fixture()
def step_context():
    return {
        "username": "",
        "password": ""
    }


@given("I'm A Standard User")
def test_standard_user(credentials, step_context):
    username, password = credentials
    step_context["username"] = username
    step_context["password"] = password


@when("I Am On The Login Page")
def test_user_is_on_login_page(page, step_context, context):
    page = context.new_page()
    login_page = LoginPage.LoginPage(page)
    login_page.open_login_page()
    login_page.login_to_the_environment(
        step_context["username"], step_context["password"]
    )


@then("I Should Be Able To Login With My Credentials")
def test_products_page_is_displayed(page):
    login_page = LoginPage.LoginPage(page)
    login_page.main_page_is_present()
