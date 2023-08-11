import pytest
from pytest_bdd import scenario, given, when, then


@pytest.fixture(scope="class")
def step_context():
    return {
        "username": "",
        "password": ""
    }


@scenario("../features/login_page.feature", "Login To The Store Page")
def test_login_to_the_page():
    # used for integration with bdd
    pass


@given("I'm A Standard User")
def standard_user(credentials, step_context):
    username, password = credentials
    step_context["username"] = username
    step_context["password"] = password


@when("I Am On The Login Page")
def user_is_on_login_page(step_context, login_page):
    login_page.open_login_page()
    login_page.login_to_the_environment(
        step_context["username"], step_context["password"]
    )


@then("I Should Be Able To Login With My Credentials")
def products_page_is_displayed(login_page):
    login_page.main_page_is_present()
