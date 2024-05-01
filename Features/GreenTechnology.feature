Feature: Green Technology Adoption

  Scenario: User logs into the sustainable living app
    Given the user is on the sustainable living app login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be successfully logged in
    And redirected to the sustainable living app's dashboard

  Background:
    Given the user is logged into the sustainable living app

  Scenario: User tracks and reduces carbon footprint
    When the user uses the app to track daily activities impacting the environment
    And receives recommendations for reducing carbon footprint
    Then the app should provide insights and progress tracking

  Scenario: User explores eco-friendly product options
    When the user searches for eco-friendly products
    And makes sustainable choices while shopping
    Then the app should provide information and recommendations

  Scenario: User logs out of the sustainable living app
    When the user clicks on the logout button
    Then the user should be successfully logged out
    And redirected to the sustainable living app's login page
