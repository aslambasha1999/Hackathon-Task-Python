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

@given(r"the user is on the social media login page")
def the_user_is_on_the_social_media_login_page(context):
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

@then(r"redirected to the social media platform's homepage")
def redirected_to_the_social_media_platforms_homepage(context):
    # Add your code here
    pass

@given(r"the user is logged into the social media platform")
def the_user_is_logged_into_the_social_media_platform(context):
    # Add your code here
    pass

@when(r"the user clicks on the post creation button")
def the_user_clicks_on_the_post_creation_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@when(r"enters text for the post")
def enters_text_for_the_post(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"clicks the post button")
def clicks_the_post_button(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.click()

@then(r"the text post should be successfully published")
def the_text_post_should_be_successfully_published(context):
    # Add your code here
    pass

@when(r"uploads a photo")
def uploads_a_photo(context):
    # Add your code here
    pass

@when(r"adds a caption")
def adds_a_caption(context):
    # Add your code here
    pass

@then(r"the photo post should be successfully published")
def the_photo_post_should_be_successfully_published(context):
    # Add your code here
    pass

@given(r"the user has a post on their timeline")
def the_user_has_a_post_on_their_timeline(context):
    # Add your code here
    pass

@when(r"the user selects the post to hide")
def the_user_selects_the_post_to_hide(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@when(r"chooses the hide option")
def chooses_the_hide_option(context):
    # Add your code here
    pass

@then(r"the post should no longer be visible on the user's timeline")
def the_post_should_no_longer_be_visible_on_the_users_timeline(context):
    # Add your code here
    pass

@then(r"the post can be found in the user's hidden posts section")
def the_post_can_be_found_in_the_users_hidden_posts_section(context):
    # Add your code here
    pass

