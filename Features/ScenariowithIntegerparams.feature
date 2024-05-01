Feature: Integer params
Scenario: Add item to cart with price
  Given I am on the product page
  When I add 2 items with price $10 to my cart
  Then it should reflect in my cart total
