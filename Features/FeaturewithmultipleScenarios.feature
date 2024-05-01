Feature: Search
  Scenario: Search with valid keyword
    Given I am on the search page
    When I enter "apple" in the search field
    And I click the search button
    Then I should see relevant search results

  Scenario: Search with invalid keyword
    Given I am on the search page
    When I enter "@#$%" in the search field
    And I click the search button
    Then I should see a message indicating no results found