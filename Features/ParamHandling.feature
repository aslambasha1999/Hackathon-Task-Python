Feature: All types of Parameters Handling

    Scenario: Withdraw cash from ATM
        Given a customer has an 'account' balance of $100
        When the customer withdraws $20 from the ATM
        Then the "account" balance should be $80

    Scenario Outline: Search for different terms
        Given the user is on the search page
        When the user searches for <term>
        Then results for <term> are displayed

        Examples:
            | term     |
            | Behave   |
            | Cucumber |
            | Selenium |

Scenario: Add items to the shopping cart
   Given a customer adds the following items to the cart:
        | Item    | Quantity |
        | Apples  | 3        |
        | Bananas | 2        |
        | Oranges | 4        |
    When the customer checks out
    Then the shopping cart should contain the following items:

