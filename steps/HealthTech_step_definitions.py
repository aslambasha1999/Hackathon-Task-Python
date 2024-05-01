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

@given(r"the user is on the health tracking app login page")
def the_user_is_on_the_health_tracking_app_login_page(context):
    # Add your code here
    pass

@when(r"the user enters valid credentials")
def the_user_enters_valid_credentials(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"clicks the login button")
def clicks_the_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the user should be successfully logged in")
def the_user_should_be_successfully_logged_in(context):
    # Add your code here
    pass

@then(r"redirected to the health tracking app's dashboard")
def redirected_to_the_health_tracking_apps_dashboard(context):
    # Add your code here
    pass

@given(r"the user is logged into the health tracking app")
def the_user_is_logged_into_the_health_tracking_app(context):
    # Add your code here
    pass

@when(r"the user records daily physical activity")
def the_user_records_daily_physical_activity(context):
    # Add your code here
    pass

@when(r"inputs vital signs such as heart rate and sleep data")
def inputs_vital_signs_such_as_heart_rate_and_sleep_data(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

	time.sleep("Add Your Argument")

@then(r"the health data should be stored and updated in the app")
def the_health_data_should_be_stored_and_updated_in_the_app(context):
    # Add your code here
    pass

@when(r"the user sets health and fitness goals")
def the_user_sets_health_and_fitness_goals(context):
    # Add your code here
    pass

@when(r"diligently works towards achieving them")
def diligently_works_towards_achieving_them(context):
    # Add your code here
    pass

@then(r"the app should track and celebrate goal achievements")
def the_app_should_track_and_celebrate_goal_achievements(context):
    # Add your code here
    pass

@when(r"the user clicks on the logout button")
def the_user_clicks_on_the_logout_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the user should be successfully logged out")
def the_user_should_be_successfully_logged_out(context):
    # Add your code here
    pass

@then(r"redirected to the health tracking app's login page")
def redirected_to_the_health_tracking_apps_login_page(context):
    # Add your code here
    pass

