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

@given(r"I am on a web page containing checkboxes")
def i_am_on_a_web_page_containing_checkboxes(context):
    # Add your code here
    pass

@when(r"I decide to check a specific checkbox")
def i_decide_to_check_a_specific_checkbox(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@when(r"I provide the checkbox element to click")
def i_provide_the_checkbox_element_to_click(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the checkbox should be checked successfully")
def the_checkbox_should_be_checked_successfully(context):
    # Add your code here
    pass

@given(r"I am on a web page containing dropdown menus")
def i_am_on_a_web_page_containing_dropdown_menus(context):
    # Add your code here
    pass

@when(r"I decide to select an option from a specific dropdown")
def i_decide_to_select_an_option_from_a_specific_dropdown(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@when(r"I provide the dropdown element and the option value to select")
def i_provide_the_dropdown_element_and_the_option_value_to_select(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@then(r"the specified option should be selected successfully")
def the_specified_option_should_be_selected_successfully(context):
    # Add your code here
    pass

@given(r"I am on a web page with vertical content")
def i_am_on_a_web_page_with_vertical_content(context):
    # Add your code here
    pass

@when(r"I decide to scroll down by a specific amount")
def i_decide_to_scroll_down_by_a_specific_amount(context):
	context.driver.execute_script("window.scrollBy(0, 250);")

@when(r"I provide the vertical scroll value")
def i_provide_the_vertical_scroll_value(context):
	context.driver.execute_script("window.scrollBy(0, 250);")

@then(r"the page should be scrolled down successfully")
def the_page_should_be_scrolled_down_successfully(context):
    # Add your code here
    pass

@given(r"I am on a web page with elements")
def i_am_on_a_web_page_with_elements(context):
    # Add your code here
    pass

@when(r"I decide to scroll to a specific element")
def i_decide_to_scroll_to_a_specific_element(context):
	context.driver.execute_script("window.scrollBy(0, 250);")

@when(r"I provide the element to scroll to")
def i_provide_the_element_to_scroll_to(context):
	context.driver.execute_script("window.scrollBy(0, 250);")

@then(r"the page should be scrolled to the specified element successfully")
def the_page_should_be_scrolled_to_the_specified_element_successfully(context):
    # Add your code here
    pass

@given(r"I am on a web page with interactive elements")
def i_am_on_a_web_page_with_interactive_elements(context):
    # Add your code here
    pass

@when(r"I decide to move to a specific element")
def i_decide_to_move_to_a_specific_element(context):
    # Add your code here
    pass

@when(r"I provide the element to move to")
def i_provide_the_element_to_move_to(context):
    # Add your code here
    pass

@then(r"the cursor should hover over the specified element")
def the_cursor_should_hover_over_the_specified_element(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	ActionChains(context.driver).move_to_element(element).perform()

@given(r"I am on a web page with input fields")
def i_am_on_a_web_page_with_input_fields(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I decide to clear a specific input field")
def i_decide_to_clear_a_specific_input_field(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.clear()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I provide the input field element to clear")
def i_provide_the_input_field_element_to_clear(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.clear()

@then(r"the input field should be cleared successfully")
def the_input_field_should_be_cleared_successfully(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@then(r"when I decide to reset the input field")
def when_i_decide_to_reset_the_input_field(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.clear()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@then(r"the input field should be reset successfully")
def the_input_field_should_be_reset_successfully(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.clear()

@given(r"I am on a web page")
def i_am_on_a_web_page(context):
    # Add your code here
    pass

@when(r"I decide to refresh the page")
def i_decide_to_refresh_the_page(context):
	context.driver.refresh()

@then(r"the page should be refreshed successfully")
def the_page_should_be_refreshed_successfully(context):
    # Add your code here
    pass

@then(r"when I decide to navigate back")
def when_i_decide_to_navigate_back(context):
	context.driver.back()

@then(r"the page should navigate back successfully")
def the_page_should_navigate_back_successfully(context):
	context.driver.back()

@then(r"when I decide to navigate forward")
def when_i_decide_to_navigate_forward(context):
	context.driver.forward()

@then(r"the page should navigate forward successfully")
def the_page_should_navigate_forward_successfully(context):
	context.driver.forward()

