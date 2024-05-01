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

@given(r"I am on the home page")
def i_am_on_the_home_page(context):
    # Add your code here
    pass

@given(r"I assert pagetitle is {arg1}")
def i_assert_pagetitle_is_home_page(context,arg1):
	assert "expected_value" ==arg1

@when(r"I wait for element present with id {arg1}")
def i_wait_for_element_present_with_id_header(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	WebDriverWait(context.driver, timeout).until(expected_conditions.presence_of_element_located(("Add Your Locator")))

@then(r"I should see the header element displayed")
def i_should_see_the_header_element_displayed(context):
    # Add your code here
    pass

