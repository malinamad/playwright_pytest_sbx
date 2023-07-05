class InstancePage:
    def __init__(self, page):
        self.page = page

    def navigate_to_website(self, website):
        self.page.goto(website)

    def fill_form(self, username, password):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)

    def take_screenshot(self, path):
        self.page.screenshot(path=path)
