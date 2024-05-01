Feature: Frame and Window Management

  Scenario: Switch to a frame on the web page
    Given I am on a web page containing frames
    When I decide to switch to a specific frame
    And I provide the frame element to switch to
    Then I should be able to interact with elements within the frame

  Scenario: Switch to a new browser window
    Given I have multiple browser windows open
    When I decide to switch to a new window
    And I provide the window handle to switch to
    Then I should be able to interact with elements within the new window

  Scenario: Switch back to default content from a frame
    Given I am currently within a frame on the web page
    When I decide to switch back to the default content
    Then I should be able to interact with elements on the main page