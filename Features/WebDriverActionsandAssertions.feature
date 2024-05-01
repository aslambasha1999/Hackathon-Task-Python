Feature: WebDriver Actions and Assertions

    Scenario: Resize the browser window
    Given I am using a web browser
    When I decide to resize the browser window
    And I provide the width and height dimensions
    Then the browser window should be resized successfully

  Scenario: Close the browser window
    Given I have a web browser window open
    When I decide to close the browser window
    Then the browser window should be closed successfully

  Scenario: Quit the WebDriver
    Given I have initiated the WebDriver session
    When I decide to quit the WebDriver
    Then the WebDriver session should be terminated successfully

  Scenario: Handle a browser alert
    Given there is a browser alert
    When I decide to switch to the alert
    Then I should be able to interact with the alert successfully

  Scenario: Execute JavaScript code on the web page
    Given I am on a web page
    When I decide to execute a JavaScript code
    And I provide the JavaScript code
    Then the code should be executed successfully on the web page

  Scenario: Wait for the presence of a specific element
    Given I am on a web page
    When I decide to wait for a specific element to be present
    And I provide the locator for the element
    Then the script should wait until the element is present

  Scenario: Pause execution for a specified duration
    Given I am running a script
    When I decide to pause execution
    And I provide the duration to sleep
    Then the script should pause execution for the specified duration

  Scenario: Assert and verify values on the web page
    Given I am on a web page
    When I decide to assert a specific value
    And I provide the expected and actual values
    Then the script should assert that the values match
    And I can use the "verify" keyword for a non-fatal check

  Scenario: Assert and verify values on the web page
    Given I am on a web page
    When I decide to assert a specific value
    And I provide the expected and actual values
    Then the script should assert that the values match
    And I can use the "verify" keyword for a non-fatal check

  Scenario: Retrieve text and attribute values from an element
    Given I am on a web page with elements
    When I decide to get the text and attribute values
    And I provide the element
    Then the script should retrieve the text and attribute values successfully
