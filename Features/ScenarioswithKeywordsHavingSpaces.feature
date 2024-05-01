Feature: Scenarios with keywords having spaces
Scenario: Validate Page Elements
  Given I am on the home page
  And I assert pagetitle is "Home Page"
  When I wait for element present with id "header"
  Then I should see the header element displayed
