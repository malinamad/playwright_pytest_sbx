@products_page
Feature: Products Page
    As a user,
    I want to be able to select products in the store,
    So I will be able to proceed to the checkout.

  @ONS-4
  Scenario Outline: User Adds Product To The Cart
    Given I'm A Standard User That Is On Main Page
    When I Add A <product_name> Product To The Cart
    Then The <product_name> Product Is Present In The Cart

    Examples:
      |           product_name            |
      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Sauce Labs Onesie                 |
      | Test.allTheThings() T-Shirt (Red) |

  @ONS-10
  Scenario Outline: The Added Product Is Shown On The Cart Count
    Given I'm A Standard User That Is On Main Page
    When I Add A <product_name> Product To The Cart
    Then The Count On The Cart Is Reflected With The Added Product

    Examples:
      |           product_name            |
      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Sauce Labs Onesie                 |
      | Test.allTheThings() T-Shirt (Red) |
