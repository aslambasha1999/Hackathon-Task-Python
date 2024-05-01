Feature: Social Media Interaction

  Scenario: User logs into the social media platform
    Given the user is on the social media login page
    When the user enters valid credentials
    And clicks the login button
    Then the user should be successfully logged in
    And redirected to the social media platform's homepage

  Background:
    Given the user is logged into the social media platform

  Scenario: User creates a text post
    When the user clicks on the post creation button
    And enters text for the post
    And clicks the post button
    Then the text post should be successfully published

  Scenario: User uploads and shares a photo
    When the user clicks on the post creation button
    And uploads a photo
    And adds a caption
    And clicks the post button
    Then the photo post should be successfully published

  Scenario: User hides a post from their timeline
    Given the user has a post on their timeline
    When the user selects the post to hide
    And chooses the hide option
    Then the post should no longer be visible on the user's timeline
    And the post can be found in the user's hidden posts section
