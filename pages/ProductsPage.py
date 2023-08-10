from playwright.sync_api import expect


class ProductsPage:
    """ The class is created in order to have the related methods
    of the main page to work with products. """

    all_items_list = []
    missing_product_err_msg = ("The provided product "
                               "is not present on the actual items list.")

    def __init__(self, page):
        self.page = page
        self.products_container = page.locator(".inventory_list")
        self.shopping_cart = page.locator("#shopping_cart_container")
        self.product_in_cart = page.locator(".inventory_item_name")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    def get_all_products(self) -> None:
        """ Return all the products in list with dictionaries format
        that are present on the main page. """

        items_div_box = self.page.locator(".inventory_item").all()

        for item in items_div_box:
            item_name = item.locator(".inventory_item_name")
            item_price = item.locator(".inventory_item_price")
            item_desc = item.locator(".inventory_item_desc")
            item_button_id = (item
                              .locator(".btn_primary")
                              .get_attribute("id"))

            self._verify_product_is_present_on_page(
                item_name, item_price, item_desc)

            self.all_items_list.append({
                "item_name": item_name.text_content(),
                "item_price": item_price.text_content(),
                "item_desc": item_desc.text_content(),
                "button_id": item_button_id,
            })

    @staticmethod
    def _verify_product_is_present_on_page(*args: str) -> None:
        """ Assert a product that should be visible on the page. """

        for item in list(args):
            expect(item).to_be_visible()

    def select_a_product(self, product_name: str) -> None:
        """ Select a product if it is present on the main page,
        otherwise raise an exception. """

        if self._verify_the_product_is_in_list(product_name):
            button_id = self._get_product_id(product_name)
            button_id_loc = self.page.locator(f"#{button_id}")
            button_id_loc.click()
        else:
            raise NameError(self.missing_product_err_msg)

    def _verify_the_product_is_in_list(self, product_name: str) -> bool:
        """ Return bool value indicating whether the provided product is
        present on the main page by looping through the retrieved data
        from the main page.

        Note: the product name is taken from the json file as test data. """

        for item in self.all_items_list:
            if item["item_name"] == product_name:
                return True
        return False

    def _get_product_id(self, product_name: str) -> str:
        """ Return button id locator by looping through the retrieved data from
        the main page of a requested product. """

        for item in self.all_items_list:
            if item["item_name"] == product_name:
                return item["button_id"]

    def proceed_to_the_cart(self) -> None:
        self.shopping_cart.click()

    def item_count_on_shopping_cart_badge_assertion(
            self, products_amount: int
    ) -> None:
        """ Assert whether the amount of products is displayed in accordance
         with the added amount. """

        expect(self.shopping_cart_badge).to_be_visible()
        expect(self.shopping_cart_badge).to_have_text(str(products_amount))

    # TODO checkout related, to refactor
    def selected_item_in_the_cart_assertion(self, products_name: str) -> None:
        expect(self.product_in_cart).to_be_visible()
        expect(self.product_in_cart).to_contain_text(products_name)

    # TODO checkout related, to refactor
    def get_list_of_all_added_products(self):
        # TODO: in case there is more than one item in the cart,
        #  retrieve list with all of them
        pass
