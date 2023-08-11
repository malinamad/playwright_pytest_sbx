from playwright.sync_api import expect


class LoginPage:
    # add to env setup
    env_url = 'https://www.saucedemo.com/'

    def __init__(self, page):
        self.page = page
        self.login_input_field = page.locator("[data-test=\"username\"]")
        self.password_input_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.main_page_title = page.locator("xpath=//div[@class='app_logo']")
        self.error_message = page.locator("[data-test=\"error\"]")

    def open_login_page(self):
        self.page.goto(self.env_url)

    def login_to_the_environment(self, login, password):
        self.login_input_field.fill(login)
        self.password_input_field.fill(password)
        self.login_button.click()

    def main_page_is_present(self):
        expect(self.main_page_title).to_contain_text("Swag Labs")

    def unsuccessful_login_error_message_is_present(self):
        expect(self.error_message).to_be_visible()
        expect(
            self.error_message
        ).to_contain_text("Epic sadface: Username and password "
                          "do not match any user in this service")
