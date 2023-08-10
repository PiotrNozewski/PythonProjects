from behave import *
from selenium import webdriver


@given('browser is open')
def browserIsOpen(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('user is on login page')
def userIsOnLoginPage(context):
    context.driver.get("https://www.automationexercise.com/")


@then('user is redirected to Home page')
def userIsRedirectedToHomePage(context):
    homePage_icon = context.driver.find_element("xpath", "//div[@class='item active']//img[@alt='demo website for "
                                                         "practice']")
    assert homePage_icon.is_displayed()


@when('user clicks Signup/Login button')
def userClicksSignupLoginButton(context):
    signup_login_button = context.driver.find_element("xpath", "//a[normalize-space()='Signup / Login']")
    signup_login_button.click()


@then('user is redirected to Login/Signup page')
def userIsRedirectedToLoginSignupPage(context):
    new_user_signup_icon = context.driver.find_element("xpath",
                                                       "//h2[normalize-space()='New User Signup!']")
    assert new_user_signup_icon.is_displayed()


@when('user fills up Name and Email Address box that already exist')
def userFillsUpNameAndEmailAddressBoxThatAlreadyExist(context):
    name_input = context.driver.find_element("xpath", "//input[@placeholder='Name']")
    name_input.click()
    name_input.send_keys("Piotr")

    email_address_input = context.driver.find_element("xpath", "//input[@data-qa='signup-email']")
    email_address_input.click()
    email_address_input.send_keys("pn@gmail.com")


@when('user clicks Signup button')
def userClicksSignupButton(context):
    signup_button = context.driver.find_element("xpath", "//button[normalize-space()='Signup']")
    signup_button.click()


@then('user sees PopUp error about Email Address already exist')
def userSeesPopUpErrorAboutEmailAddressAlreadyExist(context):
    email_addresss_already_exist_icon = context.driver.find_element("xpath",
                                                                    "//p[normalize-space()='Email Address already "
                                                                    "exist!']")
    assert email_addresss_already_exist_icon.is_displayed()


@when('close browser')
def closeBrowser(context):
    context.driver.close()
