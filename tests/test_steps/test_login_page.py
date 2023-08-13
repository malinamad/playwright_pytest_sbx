import pytest
from pytest_bdd import scenarios, given, when, then
from faker import Faker


@pytest.fixture(scope="class", name="creds")
def step_context():
    return {
        "username": "",
        "password": ""
    }


@pytest.fixture(scope="function", name="faker")
def faker_instance():
    return Faker()


scenarios("../features/login_page.feature")


@given("I'm A Standard User")
def standard_user(credentials, creds):
    username, password = credentials
    creds["username"] = username
    creds["password"] = password


@when("I Am On The Login Page")
def user_is_on_login_page(login_page):
    login_page.open_login_page()


@then("I Should Be Able To Login With My Credentials")
def products_page_is_displayed(login_page, creds):
    login_page.login_to_the_environment(
        creds["username"], creds["password"]
    )
    login_page.main_page_is_present()


@when("I Provide Incorrect Username")
def provide_incorrect_username(login_page, creds, faker):
    login_page.login_to_the_environment(
        faker.user_name(), creds["password"]
    )


@when("I Provide Incorrect Password")
def provide_incorrect_password(login_page, creds, faker):
    login_page.login_to_the_environment(
        creds["username"], faker.password()
    )


@then("I Am Unable To Login To The Page")
def user_unable_to_login_in(login_page):
    login_page.unsuccessful_login_error_message_is_present()
