# Tests are no longer relevant since it does not have bdd layer,
# those were moved to the features and test steps respectively
# to remove later
#
# from utilities.utilities import take_screenshot
#
#
# def test_successful_login_to_the_environment(
#         browser, login_page, credentials
# ) -> None:
#     username, password = credentials
#     login_page.open_login_page()
#     login_page.login_to_the_environment(username, password)
#     login_page.main_page_is_present()
#
#
# def test_incorrect_password_login(
#         browser, login_page, credentials
# ) -> None:
#     username, _ = credentials
#     login_page.open_login_page()
#     login_page.login_to_the_environment(username, 'test')
#     login_page.unsuccessful_login_error_message_is_present()
#     take_screenshot(login_page.page,
#                     'unsuccessful_login_incorrect_password')
#
#
# def test_incorrect_username_login(
#         browser, login_page, credentials
# ) -> None:
#     _, password = credentials
#     login_page.open_login_page()
#     login_page.login_to_the_environment('test', password)
#     login_page.unsuccessful_login_error_message_is_present()
#     take_screenshot(login_page.page,
#                     'unsuccessful_login_incorrect_username')
