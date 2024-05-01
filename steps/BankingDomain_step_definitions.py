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

@given(r"the customer has a valid bank account")
def the_customer_has_a_valid_bank_account(context):
    # Add your code here
    pass

@when(r"the customer inserts their ATM card")
def the_customer_inserts_their_atm_card(context):
    # Add your code here
    pass

@when(r"enters the correct PIN")
def enters_the_correct_pin(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	element.send_keys("Add Your Argument")

@when(r"selects the withdrawal option")
def selects_the_withdrawal_option(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@then(r"the ATM dispenses the requested amount")
def the_atm_dispenses_the_requested_amount(context):
    # Add your code here
    pass

@then(r"updates the account balance")
def updates_the_account_balance(context):
    # Add your code here
    pass

@when(r"selects the balance inquiry option")
def selects_the_balance_inquiry_option(context):
	element =context.driver.find_element("By.YourLocator", 'Your Locator')

	Select(element).select_by_visible_text("Add Your Argument") or Select(element).select_by_value("Add Your Argument")

@then(r"the ATM displays the account balance")
def the_atm_displays_the_account_balance(context):
    # Add your code here
    pass

@given(r"sufficient funds in their account")
def sufficient_funds_in_their_account(context):
    # Add your code here
    pass

@when(r"the customer initiates a fund transfer")
def the_customer_initiates_a_fund_transfer(context):
    # Add your code here
    pass

@when(r"provides the recipient's account details")
def provides_the_recipients_account_details(context):
    # Add your code here
    pass

@then(r"the funds are transferred successfully")
def the_funds_are_transferred_successfully(context):
    # Add your code here
    pass

@then(r"the account balance is updated accordingly")
def the_account_balance_is_updated_accordingly(context):
    # Add your code here
    pass

@when(r"the customer requests a bank statement")
def the_customer_requests_a_bank_statement(context):
    # Add your code here
    pass

@then(r"the bank provides the statement for the requested period")
def the_bank_provides_the_statement_for_the_requested_period(context):
    # Add your code here
    pass

@given(r"the customer has cash to deposit")
def the_customer_has_cash_to_deposit(context):
    # Add your code here
    pass

@when(r"the customer visits the bank branch")
def the_customer_visits_the_bank_branch(context):
	context.driver.get("Add Your Argument")

@when(r"fills out a deposit slip")
def fills_out_a_deposit_slip(context):
    # Add your code here
    pass

@when(r"hands the money to the teller")
def hands_the_money_to_the_teller(context):
    # Add your code here
    pass

@then(r"the teller processes the deposit")
def the_teller_processes_the_deposit(context):
    # Add your code here
    pass

@given(r"the customer has a loan application")
def the_customer_has_a_loan_application(context):
    # Add your code here
    pass

@when(r"the customer submits the application to the bank")
def the_customer_submits_the_application_to_the_bank(context):
    # Add your code here
    pass

@then(r"the bank reviews the application")
def the_bank_reviews_the_application(context):
    # Add your code here
    pass

@then(r"informs the customer of the loan approval or rejection")
def informs_the_customer_of_the_loan_approval_or_rejection(context):
    # Add your code here
    pass

