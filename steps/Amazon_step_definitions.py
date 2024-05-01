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

@given(r"I am on the Login page URL {arg1}")
def i_am_on_the_login_page_url_https__www_amazon_in_(context,arg1):
    # Add your code here
    pass

@then(r"I click on sign in button and wait for sign in page")
def i_click_on_sign_in_button_and_wait_for_sign_in_page(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

	WebDriverWait(context.driver, timeout).until("Add Your Argument")

@then(r"I should see Sign In Page")
def i_should_see_sign_in_page(context):
    # Add your code here
    pass

@when(r"I enter username as {arg1}")
def i_enter_username_as_testusername(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"I Click on Continue button")
def i_click_on_continue_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@when(r"I enter password as {arg1}")
def i_enter_password_as_testpassword(context,arg1):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys(arg1)

@when(r"click on login button")
def click_on_login_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I am logged in")
def i_am_logged_in(context):
    # Add your code here
    pass

@then(r"I clear cart items if any")
def i_clear_cart_items_if_any(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.clear()

@then(r"I choose Electronincs>Headphones and headphones list out")
def i_choose_electronincsheadphones_and_headphones_list_out(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@then(r"I add first availabe headphone to cart")
def i_add_first_availabe_headphone_to_cart(context):
    # Add your code here
    pass

@then(r"I search {arg1} and add second available item to cart")
def i_search_macbook_pro_and_add_second_available_item_to_cart(context,arg1):
    # Add your code here
    pass

@then(r"I Select cart from home and remove the earlier added headphones")
def i_select_cart_from_home_and_remove_the_earlier_added_headphones(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@then(r"I Reduce the Quantity of the macbook pro product to one and proceed to checkout")
def i_reduce_the_quantity_of_the_macbook_pro_product_to_one_and_proceed_to_checkout(context):
    # Add your code here
    pass

@then(r"I Click on Sign out")
def i_click_on_sign_out(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"I got log out from the application and land on sign in page")
def i_got_log_out_from_the_application_and_land_on_sign_in_page(context):
    # Add your code here
    pass

@then(r"I search different {arg1} from the search bar")
def i_search_different_products_from_the_search_bar(context,arg1):
    # Add your code here
    pass

