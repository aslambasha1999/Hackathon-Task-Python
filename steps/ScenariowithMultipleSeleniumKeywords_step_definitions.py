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

@given(r"the user opens the browser and navigates to {arg1}")
def the_user_opens_the_browser_and_navigates_to_https__www_example_com_login(context,arg1):
	context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")

	context.driver.navigate.to(arg1)

@when(r"the user enters {arg1} and enters {arg2}")
def the_user_enters_username_and_enters_password(context,arg1,arg2):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg2)

@then(r"the user should be logged in successfully")
def the_user_should_be_logged_in_successfully(context):
    # Add your code here
    pass

@then(r"the user is on the product page for {arg1} and assert title")
def the_user_is_on_the_product_page_for_laptop_and_assert_title(context,arg1):
	assert context.driver.title == arg1

@when(r"the user clicks the {arg1} button")
def the_user_clicks_the_add_to_cart_button(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the product should be added to the cart")
def the_product_should_be_added_to_the_cart(context):
    # Add your code here
    pass

