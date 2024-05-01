Feature: Shopping Feature
    Scenario: Logging In
        Given the user opens the browser and navigates to "https://www.example.com/login"
        When the user enters "username" and enters "password"
        Then the user should be logged in successfully
        And the user is on the product page for "laptop" and assert title
        When the user clicks the "Add to Cart" button
        Then the product should be added to the cart