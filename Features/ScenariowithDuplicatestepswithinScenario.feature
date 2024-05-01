Scenario: Login with invalid credentials
  Given I am on the login page
  When I enter a valid username
  And I enter an invalid password
  And I click the login button
  Then I should see an error message
  When I enter an invalid username
  And I enter a valid password
  And I click the login button
  Then I should see an error message
