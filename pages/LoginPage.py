class LoginPage:
    web_login = 'https://www.saucedemo.com/'


    def __init__(self, page):
        self.page = page
        self.login_input_field = page.locator("[data-test=\"username\"]").click()
        self.password_input_field = page.locator("[data-test=\"password\"]").click()
        self.login_button = page.locator("[data-test=\"login-button\"]").click()

    def open_login_page(self):
        self.page.goto('https://www.saucedemo.com/')

    def login_to_the_environment(self, login, password):
        self.login_input_field.fill(login)
        self.password_input_field.fill(password)
        self.login_button.click()

