"""Suite with Products related tests."""
import pytest
from pages.products_page import ProductsPage
from pytest_bdd import scenarios, given, when, then, parsers


@pytest.fixture(scope="class")
def login_to_the_page(browser, login_page, credentials):
    username, password = credentials
    login_page.open_login_page()
    login_page.login_to_the_environment(username, password)
    login_page.main_page_is_present()
    yield login_page


@pytest.fixture(scope="class")
def products_page(login_to_the_page):
    products_page_instance = ProductsPage(login_to_the_page.page)
    yield products_page_instance
    products_page_instance.page.close()


scenarios("../features/products_page.feature")


@given("I'm A Standard User That Is On Main Page")
def user_is_on_main_page(products_page) -> None:
    products_page.get_all_products()


@when(parsers.parse("I Add A {product_name} Product To The Cart"))
def user_adds_a_product_to_the_cart(
        products_page, product_name
) -> None:
    products_page.add_a_product_from_main_page(product_name)


@then(parsers.parse("The {product_name} Product Is Present In The Cart"))
def verify_that_the_added_product_is_in_the_cart(
        products_page, product_name
) -> None:
    products_page.proceed_to_the_cart()
    products_page.selected_item_in_the_cart_assertion(product_name)
    products_page.page.pause()


@then("The Count On The Cart Is Reflected With The Added Product")
def verify_that_the_product_count_is_updated(
        products_page
) -> None:
    products_page.item_count_on_shopping_cart_badge_assertion(1)
