Feature: Web Page Navigation and Interaction

Feature: User Login

  Scenario: Successful Login
    Given Launch the 'login' page and navigate to 'https://www.gmail.com'
    When User Enter username 'user123'
    And User Enter password 'password123'
    And User Click on the login button
    Then User should be logged in successfully

  Scenario: Login to a web application
    Given I open the browser and navigate to 'https://www.amazon.com'
    When I enter 'john.doe@example.com' and 'password123' in the login form
    And I click on the 'Login' button
    Then I should be logged in successfully

  Scenario: Search for a product and add to the cart
    Given I open the browser and navigate to 'https://www.flipkart.com'
    When I enter 'Laptop' in the search box
    And I click on the 'Search' button
    Then I should see search results for 'Laptop'
    And I click on the first search result
    And I click on the 'Add to Cart' button
    Then the product should be added to the shopping cart
    
  Scenario: Fill out a registration form
    Given I open the browser and navigate to 'https://www.example.com/register'
    When I enter 'John Doe' in the 'Full Name' field
    And I enter 'john.doe@example.com' in the 'Email' field
    And I enter 'password123' in the 'Password' field
    And I click on the 'Register' button
    Then I should be registered successfully

  Scenario: Verify navigation menu
    Given I open the browser and navigate to 'https://www.example.com'
    Then I should see navigation links to 'Home', 'Products', 'Services', 'About Us', and 'Contact'

  Scenario: Download a file
    Given I open the browser and navigate to 'https://www.example.com/downloads'
    When I click on the 'Download Now' button
    Then the file should be downloaded successfully

  Scenario Outline: As someone who wants to sign up
    When I visit the homepage
    And I click on the Register button
    And I enter my <firstname> in the firstname input
    And I enter my <surname> in the surname input
    And I enter my <emailaddress> in the email input
    And I enter my <password> in the password input
    And I enter my <password> in the password confirmation input
    And I agree to the terms and conditions
    And I click the Submit button
    Then I expect the registration to <ExpectedResult>

    Examples:
    | firstname | surname    | emailaddress          | password       | ExpectedResult |
    | First     | User       | first@somewhere.com   |                | Fail           |
    | Second    | User       | second@somewhere.com  | .              | Fail           |
    | Third     | User       | third@somewhere.com   | toofew         | Fail           |
    | Fourth    | User       | fourth@somewhere.com  | weakpassword   | Fail           |
    | Fifth     | User       | fifth@somewhere.com   | MissingNumber  | Fail           |
    | Sixth     | User       | sixth@somewhere.com   | m1ssingc4pital | Fail           |
    | seventh   | User       | seventh@somewhere.com | CapsAndNumb3r  | Pass           |



  
  
