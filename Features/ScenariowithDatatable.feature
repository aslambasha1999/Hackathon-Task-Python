Feature:Data table scenario
Scenario: Update profile information
  Given I am on the profile page
  When I update my profile with the following details
    | Field       | Value       |
    | First Name  | John        |
    | Last Name   | Doe         |
    | Email       | john@example.com |
  And I click the save button
  Then my profile should be updated successfully
