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

@given(r"I am on the registration page")
def i_am_on_the_registration_page(context):
    # Add your code here
    pass

@when(r"I enter {email} in the email field")
def i_enter_email_in_the_email_field(context,email):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(email)

@when(r"I enter {password} in the password field")
def i_enter_password_in_the_password_field(context,password):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(password)

@when(r"click on submit button")
def click_on_submit_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.submit()

@then(r"validate the dashboard message")
def validate_the_dashboard_message(context):
    # Add your code here
    pass

