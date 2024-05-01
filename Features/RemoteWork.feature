Feature: Remote Work Collaboration

  Scenario: Employee logs into the remote work platform
    Given the employee is on the remote work platform login page
    When the employee enters valid credentials
    And clicks the login button
    Then the employee should be successfully logged in
    And redirected to the remote work platform's dashboard

  Background:
    Given the user is logged into the remote work platform

  Scenario: Employee schedules a virtual team meeting
    When the employee accesses the team collaboration tools
    And schedules a virtual team meeting
    Then the meeting details should be sent to team members
    And the virtual meeting should start on time

  Scenario: Employee updates project status in the project management tool
    When the employee accesses the project management tool
    And updates the status of assigned tasks
    Then the project status should be reflected in real-time

  Scenario: Employee logs out of the remote work platform
    When the employee clicks on the logout button
    Then the employee should be successfully logged out
    And redirected to the remote work platform's login page
