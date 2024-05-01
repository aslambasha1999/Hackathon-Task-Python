Feature: Login
  Scenario: Successful login
    Given I am on the login page
    When enter username "student" and enter password "Password123"
    And I click the login button
    Then I should be redirected to the dashboard