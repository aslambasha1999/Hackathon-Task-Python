Feature: Registration
    Scenario Outline: Register with different email domains
        Given I am on the registration page
        When I enter <email> in the email field
        And I enter <password> in the password field
        And I click the register button
        Then I should see a confirmation message

        Examples:
            | email             | password |
            | user1@example.com | pass123  |
            | user2@test.com    | password |