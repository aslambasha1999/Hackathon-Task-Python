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

@given(r"Launch the App and Click on Login Button")
def launch_the_app_and_click_on_login_button(context):
	context.driver.get("Add Your Argument")

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@when(r"Enter {arg1} UserID")
def enter_abcd_gmail_com_userid(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"Enter {numArg1} password")
def enter_12345_password(context,numArg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(numArg1)

@when(r"click on Login Button")
def click_on_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@when(r"Home page opens")
def home_page_opens(context):
	context.driver.get("Add Your Argument")

@then(r"Verify Home Screen")
def verify_home_screen(context):
	assert "expected_value" == "Add Your Argument"

@then(r"Take screenshot")
def take_screenshot(context):
    # Add your code here
    pass

