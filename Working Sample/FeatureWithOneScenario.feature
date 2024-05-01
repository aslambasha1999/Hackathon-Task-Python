Feature: Login
  Scenario: Successful login
    Given I am on the login page
    When enter username and enter password
    And I click the login button
    Then I should be redirected to the dashboard