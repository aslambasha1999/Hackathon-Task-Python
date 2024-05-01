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

@given(r"the student is on the online learning platform login page")
def the_student_is_on_the_online_learning_platform_login_page(context):
    # Add your code here
    pass

@when(r"the student enters valid credentials")
def the_student_enters_valid_credentials(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"clicks the login button")
def clicks_the_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the student should be successfully logged in")
def the_student_should_be_successfully_logged_in(context):
    # Add your code here
    pass

@then(r"redirected to the online learning platform's homepage")
def redirected_to_the_online_learning_platforms_homepage(context):
    # Add your code here
    pass

@given(r"the user is logged into the online learning platform")
def the_user_is_logged_into_the_online_learning_platform(context):
    # Add your code here
    pass

@when(r"the student accesses the course forum")
def the_student_accesses_the_course_forum(context):
    # Add your code here
    pass

@when(r"participates in a discussion")
def participates_in_a_discussion(context):
    # Add your code here
    pass

@then(r"the student's forum activity should be recorded")
def the_students_forum_activity_should_be_recorded(context):
    # Add your code here
    pass

@given(r"the student is enrolled in a course")
def the_student_is_enrolled_in_a_course(context):
    # Add your code here
    pass

@when(r"the student completes an assessment")
def the_student_completes_an_assessment(context):
    # Add your code here
    pass

@then(r"the assessment results should be recorded")
def the_assessment_results_should_be_recorded(context):
    # Add your code here
    pass

@then(r"feedback should be provided to the student")
def feedback_should_be_provided_to_the_student(context):
    # Add your code here
    pass

@when(r"the student clicks on the logout button")
def the_student_clicks_on_the_logout_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the student should be successfully logged out")
def the_student_should_be_successfully_logged_out(context):
    # Add your code here
    pass

@then(r"redirected to the online learning platform's login page")
def redirected_to_the_online_learning_platforms_login_page(context):
    # Add your code here
    pass

