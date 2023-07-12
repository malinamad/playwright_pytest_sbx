class ProductsPage:

    def __init__(self, page):
        self.products = page.locator("#inventory_container").nth(1)

    def get_product_by_name(self):
        pass
