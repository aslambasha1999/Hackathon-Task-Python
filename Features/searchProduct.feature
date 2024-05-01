Feature: Search product and Validate it from HomePage and Deals page

    Scenario Outline: Validate product is available in Home and deals page
        Given Login into application
        When Search for <product> and extract the full name from the <page>
        Then Search for same <product> in <page> and verify it exists or not
        And Log results

        Examples:
            | product | page  |
            | "tom"   | Home  |
            | "bro"   | Deals |