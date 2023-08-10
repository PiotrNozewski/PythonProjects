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
    home_page_icon = context.driver.find_element("xpath", "//div[@class='item active']//img[@alt='demo website for "
                                                          "practice']")
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
    logged_as_Piotr_icon = context.driver.find_element("xpath", '//li[10]//a[1]')
    assert logged_as_Piotr_icon.is_displayed()


@when('user clicks Logout button')
def userClicksLogoutButton(context):
    logout_button = context.driver.find_element("xpath", "//a[normalize-space()='Logout']")
    logout_button.click()


@then('user is redirected to Login page')
def userIsRedirectedToLoginPage(context):
    login_to_your_account_icon = context.driver.find_element("xpath", "//h2[normalize-space()='Login to your account']")
    assert login_to_your_account_icon.is_displayed()


@when('close browser')
def closeBrowser(context):
    context.driver.close()
