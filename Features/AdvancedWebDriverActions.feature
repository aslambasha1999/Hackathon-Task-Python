Feature: Advanced WebDriver Actions

    Scenario: Set the position of the browser window
        Given I am using a web browser
        When I decide to set the position of the browser window
        And I provide the x and y coordinates
        Then the browser window should be moved to the specified position

    Scenario: Perform drag and drop operation
        Given I am on a web page with draggable elements
        When I decide to drag a specific element
        And I provide the source and target elements
        Then the element should be successfully dropped to the target location

    Scenario: Perform double click action on an element
        Given I am on a web page with clickable elements
        When I decide to perform a double click action
        And I provide the element to double click
        Then the element should be successfully double clicked

    Scenario: Perform right click action on an element
        Given I am on a web page with clickable elements
        When I decide to perform a right click action
        And I provide the element to right click
        Then the context menu should be displayed for the element

    Scenario: Perform click and hold action on an element
        Given I am on a web page with draggable elements
        When I decide to perform a click and hold action
        And I provide the element to click and hold
        Then the element should be successfully clicked and held

    Scenario: Release a held click on an element
        Given I have performed a click and hold action
        When I decide to release the held click
        Then the held click should be released from the element

    Scenario: Navigate back and forward in browser history
        Given I am on a web page
        When I decide to navigate back and forward
        Then the browser should navigate back and forward in history

    Scenario: Upload a file using file input element
        Given I am on a web page with a file input element
        When I decide to upload a file
        And I provide the path to the file
        Then the file should be successfully uploaded

    Scenario: Zoom in and zoom out on the web page
        Given I am on a web page
        When I decide to zoom in and zoom out
        And I provide the zoom level
        Then the web page should be zoomed in and zoomed out accordingly

    Scenario: Set a cookie for the web page
        Given I am on a web page
        When I decide to set a cookie
        And I provide the cookie name and value
        Then the cookie should be set for the web page

    Scenario: Delete a cookie from the web page
        Given I am on a web page with a specific cookie set
        When I decide to delete the cookie
        And I provide the cookie name to delete
        Then the cookie should be deleted from the web page

    Scenario: Hover over an element on the web page
        Given I am on a web page with interactive elements
        When I decide to hover over a specific element
        And I provide the element to hover over
        Then the cursor should hover over the specified element

    Scenario: Highlight an element on the web page
        Given I am on a web page with elements
        When I decide to highlight a specific element
        And I provide the element to highlight
        Then the specified element should be highlighted on the web page

    Scenario: Hide and show an element on the web page
        Given I am on a web page with elements
        When I decide to hide a specific element
        And I provide the element to hide
        Then the specified element should be hidden on the web page
        And when I decide to show the hidden element
        Then the specified element should be displayed on the web page
