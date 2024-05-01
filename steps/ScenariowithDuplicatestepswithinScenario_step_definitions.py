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

@given(r"I am on the login page")
def i_am_on_the_login_page(context):
    # Add your code here
    pass

@when(r"I enter a valid username")
def i_enter_a_valid_username(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I enter an invalid password")
def i_enter_an_invalid_password(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I click the login button")
def i_click_the_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I should see an error message")
def i_should_see_an_error_message(context):
    # Add your code here
    pass

@when(r"I enter an invalid username")
def i_enter_an_invalid_username(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I enter a valid password")
def i_enter_a_valid_password(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

