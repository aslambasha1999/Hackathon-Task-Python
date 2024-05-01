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

@given(r"User launches the URL {arg1}")
def user_launches_the_url_http__the_internet_herokuapp_com_(context,arg1):
	context.driver.get(arg1)

@then(r"User verifies the title of the page")
def user_verifies_the_title_of_the_page(context):
	assert context.driver.title == "Add Your Argument"

@when(r"User clicks on A/B Testing link")
def user_clicks_on_a_b_testing_link(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"User verifies the text on the page as {arg1}")
def user_verifies_the_text_on_the_page_as_a_b_test_control(context,arg1):
	assert "expected_value" == arg1

@when(r"User navigates back to Home page and clicks on dropdown link")
def user_navigates_back_to_home_page_and_clicks_on_dropdown_link(context):
	context.driver.navigate.to("Add Your Argument")

	context.driver.back()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@when(r"User selects {arg1} from the dropdown")
def user_selects_option_1_from_the_dropdown(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text(arg1) or Select(element).select_by_value(arg1)

@then(r"User confirms if {numArg1} is selected")
def user_confirms_if_1_is_selected(context,numArg1):
    # Add your code here
    pass

@when(r"User navigates back to Home Page and clicks on Frames")
def user_navigates_back_to_home_page_and_clicks_on_frames(context):
	context.driver.navigate.to("Add Your Argument")

	context.driver.back()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"User verifies the presence of hyperlinks on the Frames Page")
def user_verifies_the_presence_of_hyperlinks_on_the_frames_page(context):
	assert "expected_value" == "Add Your Argument"

@then(r"verifies Nested Frames hyperlink")
def verifies_nested_frames_hyperlink(context):
	assert "expected_value" == "Add Your Argument"

@then(r"verifies iFrame hyperlink")
def verifies_iframe_hyperlink(context):
	assert "expected_value" == "Add Your Argument"

