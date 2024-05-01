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

@when(r"I decide to resize the browser window")
def i_decide_to_resize_the_browser_window(context):
	context.driver.set_window_size("Add width", "Add height")

@when(r"I provide the width and height dimensions")
def i_provide_the_width_and_height_dimensions(context):
    # Add your code here
    pass

@then(r"the browser window should be resized successfully")
def the_browser_window_should_be_resized_successfully(context):
    # Add your code here
    pass

@given(r"I have a web browser window open")
def i_have_a_web_browser_window_open(context):
	context.driver.get("Add Your Argument")

@when(r"I decide to close the browser window")
def i_decide_to_close_the_browser_window(context):
	context.driver.close()

@then(r"the browser window should be closed successfully")
def the_browser_window_should_be_closed_successfully(context):
    # Add your code here
    pass

@given(r"I have initiated the WebDriver session")
def i_have_initiated_the_webdriver_session(context):
    # Add your code here
    pass

@when(r"I decide to quit the WebDriver")
def i_decide_to_quit_the_webdriver(context):
	context.driver.quit()

@then(r"the WebDriver session should be terminated successfully")
def the_webdriver_session_should_be_terminated_successfully(context):
    # Add your code here
    pass

@given(r"there is a browser alert")
def there_is_a_browser_alert(context):
	context.driver.switch_to.alert

@when(r"I decide to switch to the alert")
def i_decide_to_switch_to_the_alert(context):
	context.driver.switch_to.alert

@then(r"I should be able to interact with the alert successfully")
def i_should_be_able_to_interact_with_the_alert_successfully(context):
	context.driver.switch_to.alert

@given(r"I am on a web page")
def i_am_on_a_web_page(context):
    # Add your code here
    pass

@when(r"I decide to execute a JavaScript code")
def i_decide_to_execute_a_javascript_code(context):
    # Add your code here
    pass

@when(r"I provide the JavaScript code")
def i_provide_the_javascript_code(context):
    # Add your code here
    pass

@then(r"the code should be executed successfully on the web page")
def the_code_should_be_executed_successfully_on_the_web_page(context):
    # Add your code here
    pass

@when(r"I decide to wait for a specific element to be present")
def i_decide_to_wait_for_a_specific_element_to_be_present(context):
	WebDriverWait(context.driver, timeout).until("Add Your Argument")

@when(r"I provide the locator for the element")
def i_provide_the_locator_for_the_element(context):
    # Add your code here
    pass

@then(r"the script should wait until the element is present")
def the_script_should_wait_until_the_element_is_present(context):
	WebDriverWait(context.driver, timeout).until("Add Your Argument")

@given(r"I am running a script")
def i_am_running_a_script(context):
    # Add your code here
    pass

@when(r"I decide to pause execution")
def i_decide_to_pause_execution(context):
    # Add your code here
    pass

@when(r"I provide the duration to sleep")
def i_provide_the_duration_to_sleep(context):
	time.sleep("Add Your Argument")

@then(r"the script should pause execution for the specified duration")
def the_script_should_pause_execution_for_the_specified_duration(context):
    # Add your code here
    pass

@when(r"I decide to assert a specific value")
def i_decide_to_assert_a_specific_value(context):
	assert "expected_value" =="Add Your Argument"

@when(r"I provide the expected and actual values")
def i_provide_the_expected_and_actual_values(context):
    # Add your code here
    pass

@then(r"the script should assert that the values match")
def the_script_should_assert_that_the_values_match(context):
	assert "expected_value" =="Add Your Argument"

@then(r"I can use the {arg1} keyword for a non-fatal check")
def i_can_use_the_verify_keyword_for_a_non_fatal_check(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@given(r"I am on a web page with elements")
def i_am_on_a_web_page_with_elements(context):
    # Add your code here
    pass

@when(r"I decide to get the text and attribute values")
def i_decide_to_get_the_text_and_attribute_values(context):
    # Add your code here
    pass

@when(r"I provide the element")
def i_provide_the_element(context):
    # Add your code here
    pass

@then(r"the script should retrieve the text and attribute values successfully")
def the_script_should_retrieve_the_text_and_attribute_values_successfully(context):
    # Add your code here
    pass

