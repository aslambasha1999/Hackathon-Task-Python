Feature: git Login

    Scenario: Github handling
        Given User should be on github page
        When User Click on Commit
        Then User should be able to see All Modified chnages in master