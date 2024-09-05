Feature: Product Management

  Scenario: Reading a product
    Given a product exists
    When I read the product
    Then I should see the product details

  Scenario: Updating a product
    Given a product exists
    When I update the product with new details
    Then the product should be updated

  Scenario: Deleting a product
    Given a product exists
    When I delete the product
    Then the product should be deleted

  Scenario: Listing all products
    Given multiple products exist
    When I list all products
    Then I should see a list of all products

  Scenario: Searching a product by name
    Given a product exists with a specific name
    When I search for the product by name
    Then I should see the product details

  Scenario: Searching a product by category
    Given a product exists in a specific category
    When I search for products by category
    Then I should see products in that category

  Scenario: Searching a product by availability
    Given a product exists with a specific availability status
    When I search for products by availability
    Then I should see products with that availability status
