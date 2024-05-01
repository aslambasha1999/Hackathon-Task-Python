Feature: Online Learning Interaction

  Scenario: Student logs into the online learning platform
    Given the student is on the online learning platform login page
    When the student enters valid credentials
    And clicks the login button
    Then the student should be successfully logged in
    And redirected to the online learning platform's homepage

  Background:
    Given the user is logged into the online learning platform

  Scenario: Student joins a discussion forum for a course
    When the student accesses the course forum
    And participates in a discussion
    Then the student's forum activity should be recorded

  Scenario: Student completes an assessment
    Given the student is enrolled in a course
    When the student completes an assessment
    Then the assessment results should be recorded
    And feedback should be provided to the student

  Scenario: Student logs out of the online learning platform
    When the student clicks on the logout button
    Then the student should be successfully logged out
    And redirected to the online learning platform's login page
