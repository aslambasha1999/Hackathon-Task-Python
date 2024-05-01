Feature: Shopping Cart
  Scenario: Add item to cart
    Given I am logged in
    When I search for "headphones"
    And I add it to my cart
    Then I should see it in my cart

  Scenario: Remove item from cart
    Given I am logged in
    Given I have "headphones" in my cart
    When I remove it from my cart
    Then it should no longer be in my cart
