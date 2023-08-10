from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome()


@when('open google page')
def openGooglePage(context):
    context.driver.get("https://www.google.pl/")


@then('verify if the logo presents')
def step_impl(context):
    status = context.driver.find_element("xpath", "//img[@alt='Google']").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()
