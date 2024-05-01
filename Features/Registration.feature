Feature: Registration
    Scenario Outline: Register with different details
        Given I am on the registration page
        When I enter <email> in the email field
        And I enter <password> in the password field
        And click on submit button
        Then validate the dashboard message
        Examples:
            | email             | password |
            | user1@example.com | pass123  |
            | user2@test.com    | password |