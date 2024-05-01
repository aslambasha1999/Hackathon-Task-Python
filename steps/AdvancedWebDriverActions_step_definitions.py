# Auto-generated import statements

from behave import *

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from asyncio import timeout
import time

@given(r"I am using a web browser")
def i_am_using_a_web_browser(context):
    # Add your code here
    pass

@when(r"I decide to set the position of the browser window")
def i_decide_to_set_the_position_of_the_browser_window(context):
    # Add your code here
    pass

@when(r"I provide the x and y coordinates")
def i_provide_the_x_and_y_coordinates(context):
    # Add your code here
    pass

@then(r"the browser window should be moved to the specified position")
def the_browser_window_should_be_moved_to_the_specified_position(context):
    # Add your code here
    pass

@given(r"I am on a web page with draggable elements")
def i_am_on_a_web_page_with_draggable_elements(context):
    # Add your code here
    pass

@when(r"I decide to drag a specific element")
def i_decide_to_drag_a_specific_element(context):
    # Add your code here
    pass

@when(r"I provide the source and target elements")
def i_provide_the_source_and_target_elements(context):
    # Add your code here
    pass

@then(r"the element should be successfully dropped to the target location")
def the_element_should_be_successfully_dropped_to_the_target_location(context):
    # Add your code here
    pass

@given(r"I am on a web page with clickable elements")
def i_am_on_a_web_page_with_clickable_elements(context):
    # Add your code here
    pass

@when(r"I decide to perform a double click action")
def i_decide_to_perform_a_double_click_action(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).double_click(element).perform()

@when(r"I provide the element to double click")
def i_provide_the_element_to_double_click(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).double_click(element).perform()

@then(r"the element should be successfully double clicked")
def the_element_should_be_successfully_double_clicked(context):
    # Add your code here
    pass

@when(r"I decide to perform a right click action")
def i_decide_to_perform_a_right_click_action(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).context_click(element).perform()

@when(r"I provide the element to right click")
def i_provide_the_element_to_right_click(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).context_click(element).perform()

@then(r"the context menu should be displayed for the element")
def the_context_menu_should_be_displayed_for_the_element(context):
    # Add your code here
    pass

@when(r"I decide to perform a click and hold action")
def i_decide_to_perform_a_click_and_hold_action(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).click_and_hold(element).perform()

@when(r"I provide the element to click and hold")
def i_provide_the_element_to_click_and_hold(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).click_and_hold(element).perform()

@then(r"the element should be successfully clicked and held")
def the_element_should_be_successfully_clicked_and_held(context):
    # Add your code here
    pass

@given(r"I have performed a click and hold action")
def i_have_performed_a_click_and_hold_action(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).click_and_hold(element).perform()

@when(r"I decide to release the held click")
def i_decide_to_release_the_held_click(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).release(element).perform()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the held click should be released from the element")
def the_held_click_should_be_released_from_the_element(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@given(r"I am on a web page")
def i_am_on_a_web_page(context):
    # Add your code here
    pass

@when(r"I decide to navigate back and forward")
def i_decide_to_navigate_back_and_forward(context):
	context.driver.back()

	context.driver.forward()

@then(r"the browser should navigate back and forward in history")
def the_browser_should_navigate_back_and_forward_in_history(context):
	context.driver.back()

	context.driver.forward()

@given(r"I am on a web page with a file input element")
def i_am_on_a_web_page_with_a_file_input_element(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I decide to upload a file")
def i_decide_to_upload_a_file(context):
    # Add your code here
    pass

@when(r"I provide the path to the file")
def i_provide_the_path_to_the_file(context):
    # Add your code here
    pass

@then(r"the file should be successfully uploaded")
def the_file_should_be_successfully_uploaded(context):
    # Add your code here
    pass

@when(r"I decide to zoom in and zoom out")
def i_decide_to_zoom_in_and_zoom_out(context):
	context.driver.execute_script("document.body.style.zoom='zoom_level%'")

	context.driver.execute_script("document.body.style.zoom='zoom_level%'")

@when(r"I provide the zoom level")
def i_provide_the_zoom_level(context):
    # Add your code here
    pass

@then(r"the web page should be zoomed in and zoomed out accordingly")
def the_web_page_should_be_zoomed_in_and_zoomed_out_accordingly(context):
    # Add your code here
    pass

@when(r"I decide to set a cookie")
def i_decide_to_set_a_cookie(context):
    # Add your code here
    pass

@when(r"I provide the cookie name and value")
def i_provide_the_cookie_name_and_value(context):
    # Add your code here
    pass

@then(r"the cookie should be set for the web page")
def the_cookie_should_be_set_for_the_web_page(context):
    # Add your code here
    pass

@given(r"I am on a web page with a specific cookie set")
def i_am_on_a_web_page_with_a_specific_cookie_set(context):
    # Add your code here
    pass

@when(r"I decide to delete the cookie")
def i_decide_to_delete_the_cookie(context):
    # Add your code here
    pass

@when(r"I provide the cookie name to delete")
def i_provide_the_cookie_name_to_delete(context):
    # Add your code here
    pass

@then(r"the cookie should be deleted from the web page")
def the_cookie_should_be_deleted_from_the_web_page(context):
    # Add your code here
    pass

@given(r"I am on a web page with interactive elements")
def i_am_on_a_web_page_with_interactive_elements(context):
    # Add your code here
    pass

@when(r"I decide to hover over a specific element")
def i_decide_to_hover_over_a_specific_element(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).move_to_element(element).perform()

@when(r"I provide the element to hover over")
def i_provide_the_element_to_hover_over(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).move_to_element(element).perform()

@then(r"the cursor should hover over the specified element")
def the_cursor_should_hover_over_the_specified_element(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).move_to_element(element).perform()

@given(r"I am on a web page with elements")
def i_am_on_a_web_page_with_elements(context):
    # Add your code here
    pass

@when(r"I decide to highlight a specific element")
def i_decide_to_highlight_a_specific_element(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	context.driver.execute_script("arguments[0].style.border='3px solid red';", element)

@when(r"I provide the element to highlight")
def i_provide_the_element_to_highlight(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	context.driver.execute_script("arguments[0].style.border='3px solid red';", element)

@then(r"the specified element should be highlighted on the web page")
def the_specified_element_should_be_highlighted_on_the_web_page(context):
    # Add your code here
    pass

