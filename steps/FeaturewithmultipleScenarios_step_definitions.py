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

@given(r"I am on the search page")
def i_am_on_the_search_page(context):
    # Add your code here
    pass

@when(r"I enter {arg1} in the search field")
def i_enter_apple_in_the_search_field(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I click the search button")
def i_click_the_search_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I should see relevant search results")
def i_should_see_relevant_search_results(context):
    # Add your code here
    pass

@when(r"I enter {arg1} in the search field")
def i_enter______in_the_search_field(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@then(r"I should see a message indicating no results found")
def i_should_see_a_message_indicating_no_results_found(context):
    # Add your code here
    pass

