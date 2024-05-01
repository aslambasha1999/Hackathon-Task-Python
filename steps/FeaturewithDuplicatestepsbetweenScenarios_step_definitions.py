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

@given(r"I am logged in")
def i_am_logged_in(context):
    # Add your code here
    pass

@when(r"I search for {arg1}")
def i_search_for_headphones(context,arg1):
    # Add your code here
    pass

@when(r"I add it to my cart")
def i_add_it_to_my_cart(context):
    # Add your code here
    pass

@then(r"I should see it in my cart")
def i_should_see_it_in_my_cart(context):
    # Add your code here
    pass

@given(r"I have {arg1} in my cart")
def i_have_headphones_in_my_cart(context,arg1):
    # Add your code here
    pass

@when(r"I remove it from my cart")
def i_remove_it_from_my_cart(context):
    # Add your code here
    pass

@then(r"it should no longer be in my cart")
def it_should_no_longer_be_in_my_cart(context):
    # Add your code here
    pass

