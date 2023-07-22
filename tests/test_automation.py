def test_login_to_the_environment(browser, login_page, credentials) -> None:
    username, password = credentials
    login_page.open_login_page()
    login_page.login_to_the_environment(username, password)
    login_page.main_page_is_present()
    browser.close()
