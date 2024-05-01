Feature: Login
  Background:
    Given I am on the login page

  Scenario: Successful login
    When I enter username and password
    And I click the login button
    Then I should be redirected to the dashboard
