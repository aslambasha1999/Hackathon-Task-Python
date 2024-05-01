Feature: Registration
  Scenario Outline: Register with different details
    Given I am on the registration page
    When I enter <email> in the email field
    And I enter <password> in the password field
    And I enter the following details
      | Field       | Value       |
      | First Name  | <first_name> |
      | Last Name   | <last_name>  |
    And I click the register button
    Then I should see a confirmation message

  Examples:
    | email               | password | first_name | last_name |
    | user1@example.com  | pass123  | John       | Doe       |
    | user2@test.com     | password | Alice      | Smith     |
