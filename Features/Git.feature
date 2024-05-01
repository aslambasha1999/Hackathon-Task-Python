Feature: git Login

    Scenario: Github handling
        Given User should be on github page
        And user creates a repository
        And User Adds Latest changes
        When User Click on Commit
        And User pushes Changes to remote
        Then User should be able to see All Modified chnages in master