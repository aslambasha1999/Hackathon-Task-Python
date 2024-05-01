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

@when(r"enter username {arg1} and enter password {arg2}")
def enter_username_student_and_enter_password_password123(context,arg1,arg2):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg2)

@when(r"I click the login button")
def i_click_the_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I should be redirected to the dashboard")
def i_should_be_redirected_to_the_dashboard(context):
    # Add your code here
    pass

