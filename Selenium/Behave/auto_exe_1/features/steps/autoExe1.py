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
    homePage_iconCheck = context.driver.find_element("xpath",
                                                     "//div[@class='item active']//img[@alt='demo website for "
                                                     "practice']")
    assert homePage_iconCheck.is_displayed()


@when('user clicks Signup/Login button')
def userClicksSignupLoginButton(context):
    signupLogin_button = context.driver.find_element("xpath", "//a[normalize-space()='Signup / Login']")
    signupLogin_button.click()


@then('user is redirected to Login/Signup page')
def userIsRedirectedToLoginSignupPage(context):
    newUserSignup_icon = context.driver.find_element("xpath", "//h2[normalize-space()='New User Signup!']")
    assert newUserSignup_icon.is_displayed()


@when('user fills up name and email address box')
def userFillsUpNameAndEmailAddressBox(context):
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


@then('user is redirected to Enter Account Information page')
def userIsRedirectedToEnterAccountInformationPage(context):
    enter_account_information_icon = context.driver.find_element("xpath",
                                                                 "//b[normalize-space()='Enter Account Information']")
    assert enter_account_information_icon.is_displayed()


@when('user fills All The Data Needed To Proceed')
def userFillsTitleNameEmailPasswordDateofbirth(context):
    title_button = context.driver.find_element("xpath", "//input[@id='id_gender1']")
    title_button.click()

    name_input = context.driver.find_element("xpath", "//input[@id='name']")
    name_input.click()
    name_input.clear()
    name_input.send_keys("Piotr")

    password_input = context.driver.find_element("xpath", "//input[@id='password']")
    password_input.click()
    password_input.send_keys("qwe123")

    DAY_date_of_birth_dropdown = context.driver.find_element("id", "days")
    day_sixteen = Select(DAY_date_of_birth_dropdown)
    day_sixteen.select_by_value("16")

    MONTH_date_of_birth_dropdown = context.driver.find_element("id", "months")
    month_march = Select(MONTH_date_of_birth_dropdown)
    month_march.select_by_value("3")

    YEAR_date_of_birth_dropdown = context.driver.find_element("id", "years")
    year_one_nine_nine_three = Select(YEAR_date_of_birth_dropdown)
    year_one_nine_nine_three.select_by_value("1993")

    first_name_input = context.driver.find_element("xpath", "//input[@id='first_name']")
    first_name_input.click()
    first_name_input.send_keys("Piotr")

    last_name_input = context.driver.find_element("xpath", "//input[@id='last_name']")
    last_name_input.click()
    last_name_input.send_keys("Nozewski")

    address_input = context.driver.find_element("xpath", "//input[@id='address1']")
    address_input.click()
    address_input.send_keys("ImaginedOne")

    country_dropdown = context.driver.find_element("id", "country")
    countryUSA = Select(country_dropdown)
    countryUSA.select_by_value("United States")

    state_input = context.driver.find_element("xpath", "//input[@id='state']")
    state_input.click()
    state_input.send_keys("Guess")

    city_input = context.driver.find_element("xpath", "//input[@id='city']")
    city_input.click()
    city_input.send_keys("Warsaw")

    zipcode_input = context.driver.find_element("xpath", "//input[@id='zipcode']")
    zipcode_input.click()
    zipcode_input.send_keys("007-XYZ")

    mobile_input = context.driver.find_element("xpath", "//input[@id='mobile_number']")
    mobile_input.click()
    mobile_input.send_keys("123456789")


@when('user clicks Sign up for our newsletter button')
def userClickSignUpForOurNewsletter(context):
    newsletter_button = context.driver.find_element("xpath", "//input[@id='newsletter']")
    newsletter_button.click()


@when('user clicks Receive special offers from our partners button')
def userClicksReceiveSpecialOffersFromOurPartnersButton(context):
    special_offer_button = context.driver.find_element("xpath", "//input[@id='optin']")
    special_offer_button.click()


@when('user clicks Create Account button')
def userClicksCreateAccountButton(context):
    create_account_button = context.driver.find_element("xpath", "//button[normalize-space()='Create Account']")
    create_account_button.click()


@then('user is redirected to Account Created page')
def userIsRedirectedToAccountCreatedPage(context):
    account_created_icon = context.driver.find_element("xpath", "//b[normalize-space()='Account Created!']")
    assert account_created_icon.is_displayed()


@when('user clicks Continue button')
def userClickContinueButton(context):
    continue_button = context.driver.find_element("xpath", "//a[@class='btn btn-primary']")
    continue_button.click()


@when('user click Delete Account button')
def userClicksDeleteAccountButton(context):
    delete_account_button = context.driver.find_element("xpath", "//a[normalize-space()='Delete Account']")
    delete_account_button.click()


@then('user is redirected to Account Deleted page')
def userClicksDeleteAccountButton(context):
    account_deleted_icon = context.driver.find_element("xpath", "//div[@class='col-sm-9 col-sm-offset-1']")
    assert account_deleted_icon.is_displayed()


@when('close browser')
def closeBrowser(context):
    context.driver.close()
