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

@given(r"User should be on github page")
def user_should_be_on_github_page(context):
    # Add your code here
    pass

@when(r"User Click on Commit")
def user_click_on_commit(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"User should be able to see All Modified chnages in master")
def user_should_be_able_to_see_all_modified_chnages_in_master(context):
    # Add your code here
    pass

