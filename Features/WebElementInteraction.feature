Feature: Web Element Interaction

  Scenario: Check a checkbox on the web page
    Given I am on a web page containing checkboxes
    When I decide to check a specific checkbox
    And I provide the checkbox element to click
    Then the checkbox should be checked successfully

  Scenario: Select an option from a dropdown menu
    Given I am on a web page containing dropdown menus
    When I decide to select an option from a specific dropdown
    And I provide the dropdown element and the option value to select
    Then the specified option should be selected successfully

  Scenario: Scroll vertically on the web page
    Given I am on a web page with vertical content
    When I decide to scroll down by a specific amount
    And I provide the vertical scroll value
    Then the page should be scrolled down successfully

  Scenario: Scroll to a specific element on the web page
    Given I am on a web page with elements
    When I decide to scroll to a specific element
    And I provide the element to scroll to
    Then the page should be scrolled to the specified element successfully

  Scenario: Move to and hover over a specific element
    Given I am on a web page with interactive elements
    When I decide to move to a specific element
    And I provide the element to move to
    Then the cursor should hover over the specified element

  Scenario: Clear and reset an input field
    Given I am on a web page with input fields
    When I decide to clear a specific input field
    And I provide the input field element to clear
    Then the input field should be cleared successfully
    And when I decide to reset the input field
    Then the input field should be reset successfully

  Scenario: Refresh, navigate back, and forward on the web page
    Given I am on a web page
    When I decide to refresh the page
    Then the page should be refreshed successfully
    And when I decide to navigate back
    Then the page should navigate back successfully
    And when I decide to navigate forward
    Then the page should navigate forward successfully
