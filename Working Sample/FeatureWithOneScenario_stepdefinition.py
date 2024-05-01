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
	context.driver.get("https://practicetestautomation.com/practice-test-login/")

@when(r"enter username and enter password")
def enter_username_and_enter_password(context):
	element =context.driver.find_element(By.XPATH, "//input[@id='username']")

	element.send_keys("student")

	element =context.driver.find_element(By.XPATH, "//input[@id='password']")

	element.send_keys("Password123")

@when(r"I click the login button")
def i_click_the_login_button(context):
	element =context.driver.find_element(By.XPATH, "//button[@id='submit']")

	element.click()

@then(r"I should be redirected to the dashboard")
def i_should_be_redirected_to_the_dashboard(context):
    print("Successfully Logged in")

