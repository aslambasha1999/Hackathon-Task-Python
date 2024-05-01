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

@given(r"a customer has an {arg1} balance of ${numArg1}")
def a_customer_has_an_account_balance_of__100(context,arg1,numArg1):
    # Add your code here
    pass

@when(r"the customer withdraws ${numArg1} from the ATM")
def the_customer_withdraws__20_from_the_atm(context,numArg1):
    # Add your code here
    pass

@then(r"the account balance should be ${numArg1}")
def the_account_balance_should_be__80(context,numArg1):
    # Add your code here
    pass

