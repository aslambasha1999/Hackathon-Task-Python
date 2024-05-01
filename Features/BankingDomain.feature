Feature: Banking Operations

  Scenario: Customer withdraws money from ATM
    Given the customer has a valid bank account
    When the customer inserts their ATM card
    And enters the correct PIN
    And selects the withdrawal option
    Then the ATM dispenses the requested amount
    And updates the account balance

  Scenario: Customer checks account balance
    Given the customer has a valid bank account
    When the customer inserts their ATM card
    And enters the correct PIN
    And selects the balance inquiry option
    Then the ATM displays the account balance

  Scenario: Customer transfers money to another account
    Given the customer has a valid bank account
    And sufficient funds in their account
    When the customer initiates a fund transfer
    And provides the recipient's account details
    Then the funds are transferred successfully
    And the account balance is updated accordingly

  Scenario: Customer requests a bank statement
    Given the customer has a valid bank account
    When the customer requests a bank statement
    Then the bank provides the statement for the requested period

  Scenario: Customer deposits money at the bank
    Given the customer has cash to deposit
    When the customer visits the bank branch
    And fills out a deposit slip
    And hands the money to the teller
    Then the teller processes the deposit
    And updates the account balance

  Scenario: Customer applies for a bank loan
    Given the customer has a loan application
    When the customer submits the application to the bank
    Then the bank reviews the application
    And informs the customer of the loan approval or rejection
