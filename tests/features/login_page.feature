@login_page
Feature: Login Page
    As a user,
    I want to login to the store page,
    So I will be able to buy clothes.

    @successfully_login
    Scenario: Login To The Store Page
        Given I'm A Standard User
        When I Am On The Login Page
        Then I Should Be Able To Login With My Credentials

    @unsuccessful_login_incorrect_username
    Scenario: Unsuccessful Login Incorrect Username
        Given I'm A Standard User
        When I Am On The Login Page
        And I Provide Incorrect Username
        Then I Am Unable To Login To The Page

    @unsuccessful_login_incorrect_password
    Scenario: Unsuccessful Login Incorrect Password
        Given I'm A Standard User
        When I Am On The Login Page
        And I Provide Incorrect Password
        Then I Am Unable To Login To The Page
