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

@given(r"I am on a web page containing frames")
def i_am_on_a_web_page_containing_frames(context):
    # Add your code here
    pass

@when(r"I decide to switch to a specific frame")
def i_decide_to_switch_to_a_specific_frame(context):
    # Add your code here
    pass

@when(r"I provide the frame element to switch to")
def i_provide_the_frame_element_to_switch_to(context):
    # Add your code here
    pass

@then(r"I should be able to interact with elements within the frame")
def i_should_be_able_to_interact_with_elements_within_the_frame(context):
    # Add your code here
    pass

@given(r"I have multiple browser windows open")
def i_have_multiple_browser_windows_open(context):
	context.driver.get("Add Your Argument")

@when(r"I decide to switch to a new window")
def i_decide_to_switch_to_a_new_window(context):
    # Add your code here
    pass

@when(r"I provide the window handle to switch to")
def i_provide_the_window_handle_to_switch_to(context):
    # Add your code here
    pass

@then(r"I should be able to interact with elements within the new window")
def i_should_be_able_to_interact_with_elements_within_the_new_window(context):
    # Add your code here
    pass

@given(r"I am currently within a frame on the web page")
def i_am_currently_within_a_frame_on_the_web_page(context):
    # Add your code here
    pass

@when(r"I decide to switch back to the default content")
def i_decide_to_switch_back_to_the_default_content(context):
	context.driver.back()

@then(r"I should be able to interact with elements on the main page")
def i_should_be_able_to_interact_with_elements_on_the_main_page(context):
    # Add your code here
    pass

