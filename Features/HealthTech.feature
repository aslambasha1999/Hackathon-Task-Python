Feature: Health Tech Interaction

  Scenario: User logs into the health tracking app
    Given the user is on the health tracking app login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be successfully logged in
    And redirected to the health tracking app's dashboard

  Background:
    Given the user is logged into the health tracking app

  Scenario: User records daily activity and vitals
    When the user records daily physical activity
    And inputs vital signs such as heart rate and sleep data
    Then the health data should be stored and updated in the app

  Scenario: User sets and achieves health goals
    When the user sets health and fitness goals
    And diligently works towards achieving them
    Then the app should track and celebrate goal achievements

  Scenario: User logs out of the health tracking app
    When the user clicks on the logout button
    Then the user should be successfully logged out
    And redirected to the health tracking app's login page
