from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    # Configure WebDriverManager to automatically download and manage ChromeDriver
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def after_all(context):
    # Quit ChromeDriver
    context.driver.quit()
