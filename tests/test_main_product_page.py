import pytest
from playwright_pytest_sbx.pages import ProductsPage


@pytest.fixture()
def login_to_the_page(browser, login_page, credentials):
    username, password = credentials
    login_page.open_login_page()
    login_page.login_to_the_environment(username, password)
    login_page.main_page_is_present()
    yield login_page
    

@pytest.fixture()
def products_page(login_to_the_page):
    products_page = ProductsPage.ProductsPage(login_to_the_page.page)
    yield products_page
    products_page.page.close()


def test_add_a_product_to_the_cart(products_page) -> None:
    products_page.get_all_products()
    # TODO select random product from the json
    products_page.add_a_product_from_main_page("Sauce Labs Backpack")
    products_page.proceed_to_the_cart()
    products_page.selected_item_in_the_cart_assertion("Sauce Labs Backpack")


def test_shopping_badge_count_verification(products_page) -> None:
    products_page.get_all_products()
    # TODO select random product from the json
    products_page.add_a_product_from_main_page("Sauce Labs Backpack")
    products_page.item_count_on_shopping_cart_badge_assertion(1)
