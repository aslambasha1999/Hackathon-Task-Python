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

@given(r"Launch the {arg1} page and navigate to {arg2}")
def launch_the_login_page_and_navigate_to_https__www_gmail_com(context,arg1,arg2):
	context.driver.get(arg1)

	context.driver.navigate.to(arg2)

@when(r"User Enter username {arg1}")
def user_enter_username_user123(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"User Enter password {arg1}")
def user_enter_password_password123(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"User Click on the login button")
def user_click_on_the_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"User should be logged in successfully")
def user_should_be_logged_in_successfully(context):
    # Add your code here
    pass

@given(r"I open the browser and navigate to {arg1}")
def i_open_the_browser_and_navigate_to_https__www_amazon_com(context,arg1):
	context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")

	context.driver.navigate.to(arg1)

@when(r"I enter {arg1} and {arg2} in the login form")
def i_enter_john_doe_example_com_and_password123_in_the_login_form(context,arg1,arg2):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I click on the {arg1} button")
def i_click_on_the_login_button(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I should be logged in successfully")
def i_should_be_logged_in_successfully(context):
    # Add your code here
    pass

@given(r"I open the browser and navigate to {arg1}")
def i_open_the_browser_and_navigate_to_https__www_flipkart_com(context,arg1):
	context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")

	context.driver.navigate.to(arg1)

@when(r"I enter {arg1} in the search box")
def i_enter_laptop_in_the_search_box(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I click on the {arg1} button")
def i_click_on_the_search_button(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I should see search results for {arg1}")
def i_should_see_search_results_for_laptop(context,arg1):
    # Add your code here
    pass

@then(r"I click on the first search result")
def i_click_on_the_first_search_result(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I click on the {arg1} button")
def i_click_on_the_add_to_cart_button(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the product should be added to the shopping cart")
def the_product_should_be_added_to_the_shopping_cart(context):
    # Add your code here
    pass

@given(r"I open the browser and navigate to {arg1}")
def i_open_the_browser_and_navigate_to_https__www_example_com_register(context,arg1):
	context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")

	context.driver.navigate.to(arg1)

@when(r"I enter {arg1} in the {arg2} field")
def i_enter_john_doe_in_the_full_name_field(context,arg1,arg2):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I enter {arg1} in the {arg2} field")
def i_enter_john_doe_example_com_in_the_email_field(context,arg1,arg2):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I enter {arg1} in the {arg2} field")
def i_enter_password123_in_the_password_field(context,arg1,arg2):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I click on the {arg1} button")
def i_click_on_the_register_button(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I should be registered successfully")
def i_should_be_registered_successfully(context):
    # Add your code here
    pass

@given(r"I open the browser and navigate to {arg1}")
def i_open_the_browser_and_navigate_to_https__www_example_com(context,arg1):
	context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")

	context.driver.navigate.to(arg1)

@then(r"I should see navigation links to {arg1}, {arg2}, {arg3}, {arg4}, and {arg5}")
def i_should_see_navigation_links_to_home__products__services__about_us__and_contact(context,arg1,arg2,arg3,arg4,arg5):
    # Add your code here
    pass

@given(r"I open the browser and navigate to {arg1}")
def i_open_the_browser_and_navigate_to_https__www_example_com_downloads(context,arg1):
	context.driver = webdriver.Chrome(executable_path="Your chromedriver.exe Path")

	context.driver.navigate.to(arg1)

@when(r"I click on the {arg1} button")
def i_click_on_the_download_now_button(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the file should be downloaded successfully")
def the_file_should_be_downloaded_successfully(context):
    # Add your code here
    pass

@when(r"I visit the homepage")
def i_visit_the_homepage(context):
	context.driver.get("Add Your Argument")

@when(r"I enter my {firstname} in the firstname input")
def i_enter_my_firstname_in_the_firstname_input(context,firstname):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(firstname)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I enter my {surname} in the surname input")
def i_enter_my_surname_in_the_surname_input(context,surname):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(surname)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I enter my {emailaddress} in the email input")
def i_enter_my_emailaddress_in_the_email_input(context,emailaddress):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(emailaddress)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I enter my {password} in the password input")
def i_enter_my_password_in_the_password_input(context,password):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(password)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I enter my {password} in the password confirmation input")
def i_enter_my_password_in_the_password_confirmation_input(context,password):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(password)

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"I agree to the terms and conditions")
def i_agree_to_the_terms_and_conditions(context):
    # Add your code here
    pass

@when(r"I click the Submit button")
def i_click_the_submit_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.submit()

@then(r"I expect the registration to {ExpectedResult}")
def i_expect_the_registration_to_expectedresult(context,ExpectedResult):
    # Add your code here
    pass

