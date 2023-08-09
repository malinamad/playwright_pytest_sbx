@login_page
Feature: Login Page
    As a user,
    I want to login to the store page,
    So I will be able to buy clothes.

    Scenario: Login To The Store Page
        Given I'm A Standard User
        When I Am On The Login Page
        Then I Should Be Able To Login With My Credentials
