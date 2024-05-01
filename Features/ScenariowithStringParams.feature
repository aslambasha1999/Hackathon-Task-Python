Feature: String Params
Scenario: Search for items with special characters
  Given I am on the search page
  When I enter "item's name: test" in the search field
  And I click the search button
  Then I should see results for "item's name: test"
