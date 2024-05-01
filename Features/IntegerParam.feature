Feature: Withdraw Money

Scenario: Withdraw cash from ATM
    Given a customer has an "account" balance of $100
    When the customer withdraws $20 from the ATM
    Then the account balance should be $80
