from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select


@given('browser is open')
def browserIsOpen(context):
    context.driver = webdriver.Chrome()


@when('user is on login page')
def userIsOnLoginPage(context):
    context.driver.get("https://automationexercise.com/")


@then('user is redirected to Home page')
def userIsRedirectedToHomePage(context):
    home_page_icon = context.driver.find_element("xpath", "//div[@class='item active']//span[1]")
    assert home_page_icon.is_displayed()


@when('user clicks Signup/Login button')
def userClicksSignupLoginButton(context):
    signup_login_button = context.driver.find_element("xpath", "//a[normalize-space()='Signup / Login']")
    signup_login_button.click()


@then('user is redirected to Login/Signup page')
def userIsRedirectedToLoginSignupPage(context):
    login_to_your_account_icon = context.driver.find_element("xpath",
                                                             "//h2[normalize-space()='Login to your account']")
    assert login_to_your_account_icon.is_displayed()


@when('user fills up Email Address and Password box')
def userFillsUpEmailAddressAndPasswordBox(context):
    email_address_input = context.driver.find_element("xpath", "//input[@data-qa='login-email']")
    email_address_input.click()
    email_address_input.send_keys("pn@gmail.com")

    password_input = context.driver.find_element("xpath", "//input[@placeholder='Password']")
    password_input.click()
    password_input.send_keys("qwe123")


@when('user clicks Login button')
def userClicksLoginButton(context):
    login_button = context.driver.find_element("xpath", "//button[normalize-space()='Login']")
    login_button.click()


@then('user is redirected to Home page as logged user')
def userIsRedirectedToHomePageAsLoggedUser(context):
    logged_as_Piotr_icon = context.driver.find_element("xpath", "//li[10]//a[1]")
    assert logged_as_Piotr_icon.is_displayed()


@when('user clicks Delete Account button')
def userClicksDeleteAccountButton(context):
    delete_account_button = context.driver.find_element("xpath", "//a[normalize-space()='Delete Account']")
    delete_account_button.click()


@then('user is redirected to Account Deleted page')
def userIsRedirectedToAccountDeletedPage(context):
    account_deleted_icon = context.driver.find_element("xpath", "//b[normalize-space()='Account Deleted!']")
    assert account_deleted_icon.is_displayed()


@when('close browser')
def closeBrowser(context):
    context.driver.close()
