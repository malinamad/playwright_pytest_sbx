class CheckoutPage:

    def __init__(self, page):
        self.checkout_button = page.locator("#shopping_cart_container a")

    def proceed_to_the_checkout(self):
        self.checkout_button.click()
