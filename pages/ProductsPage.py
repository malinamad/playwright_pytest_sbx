from pprint import pprint

from playwright.sync_api import expect

class ProductsPage:
    """ The class is created in order to have the related methods of the main page
    to work with products. """

    all_items_list = []

    def __init__(self, page):
        self.page = page
        self.products_container = page.locator(".inventory_list")

    def get_all_products(self) -> None:
        """ Return all the products in list with dictionaries format
        that are present on the main page. """

        items_div_box = self.page.locator(".inventory_item").all()

        for item in items_div_box:
            item_name = item.locator(".inventory_item_name")
            item_price = item.locator(".inventory_item_price")
            item_desc = item.locator(".inventory_item_desc")

            self.verify_product_is_present_on_page_(item_name, item_price, item_desc)

            self.all_items_list.append({
                "item_name": item_name.text_content(),
                "item_price": item_price.text_content(),
                "item_desc": item_desc.text_content(),
            })

    def verify_product_is_present_on_page_(self, *args: str) -> None:
        """ Assert a product that should be visible on the page. """

        for item in list(args):
            expect(item).to_be_visible()

    def select_a_product(self, product_name: str) -> None:
        if self.verify_the_product_is_in_list_(product_name):
            # TODO get button attribute/locator, then have it clicked
            self.page.locator("")
        else:
            raise NameError("The provided product is not present on the actual items list.")

    def verify_the_product_is_in_list_(self, product_name: str) -> bool:
        for item in self.all_items_list:
            if item["item_name"] == product_name:
                return True
        return False



    # def compare_products_between_expected_and_actual(
    #         self,
    #         expected_items: list,
    #         actual_items: list
    # ):
    #     for expected_item in expected_items:
    #         expect.

# def save_elements_to_file(self, text):
#     for item in text:
#         with open('file.txt', 'w+') as f:
#             f.write(item + '\n')
