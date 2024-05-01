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

@given(r"Login into application")
def login_into_application(context):
    # Add your code here
    pass

@when(r"Search for {product} and extract the full name from the {page}")
def search_for_product_and_extract_the_full_name_from_the_page(context,product,page):
    # Add your code here
    pass

@then(r"Search for same {product} in {page} and verify it exists or not")
def search_for_same_product_in_page_and_verify_it_exists_or_not(context,product,page):
	assert "expected_value" == product

@then(r"Log results")
def log_results(context):
    # Add your code here
    pass

