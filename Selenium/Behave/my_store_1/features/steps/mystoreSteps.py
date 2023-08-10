from behave import *
from selenium import webdriver


@given('browser is open')
def browserIsOpen(context):
    context.driver = webdriver.Chrome()


@when('user is on login page')
def userIsOnLoginPage(context):
    context.driver.get("https://mystore-testlab.coderslab.pl/index.php")


@when('user clicks on Sign in button')
def userClickOnSignInButton(context):
    signIn_button = context.driver.find_element("xpath", "//span[normalize-space()='Sign in']")
    signIn_button.click()


@when('user fills up email and password box')
def userFillUpEmailAndPasswordBox(context):
    email_input = context.driver.find_element("xpath", "//input[@id='field-email']")
    email_input.click()
    email_input.send_keys("piotreknozewski@gmail.com")

    password_input = context.driver.find_element("xpath", "//input[@id='field-password']")
    password_input.click()
    password_input.send_keys("Qwerty123")


@when('user clicks SIGN IN button')
def userClickSIGNINButton(context):
    sIGNIN_button = context.driver.find_element("xpath", "//button[@id='submit-login']")
    sIGNIN_button.click()


@then('user is redirected to Your account page')
def userIsRedirectedToYourAccountPage(context):
    signout_button = context.driver.find_element("xpath", "//a[@class='logout hidden-sm-down']")
    assert signout_button.is_displayed()


@when('user clicks ADDRESSES button')
def userClickADDRESSESButton(context):
    aDDRESSES_button = context.driver.find_element("xpath", "//i[contains(text(),'')]")
    aDDRESSES_button.click()


@when('user clicks PlusCreateNewAddress button')
def userClickPlusNewAddressButton(context):
    plusNewAddress_button = context.driver.find_element("xpath", "//span[normalize-space()='Create new address']")
    plusNewAddress_button.click()


@when('user fills up New address form')
def userFillsUpNewaddressForm(context):
    data = context.table

    alias_input = context.driver.find_element("xpath", "//input[@id='field-alias']")
    alias_input.send_keys(data[0]['Alias'])

    company_input = context.driver.find_element("xpath", "//input[@id='field-company']")
    company_input.send_keys(data[0]['Company'])

    vatNumber_input = context.driver.find_element("xpath", "//input[@id='field-vat_number']")
    vatNumber_input.send_keys(data[0]['VAT number'])

    address_input = context.driver.find_element("xpath", "//input[@id='field-address1']")
    address_input.send_keys(data[0]['Address'])

    addressComp_input = context.driver.find_element("xpath", "//input[@id='field-address2']")
    addressComp_input.send_keys(data[0]['Address Complement'])

    city_input = context.driver.find_element("xpath", "//input[@id='field-city']")
    city_input.send_keys(data[0]['City'])

    zipPostalCode_input = context.driver.find_element("xpath", "//input[@id='field-postcode']")
    zipPostalCode_input.send_keys(data[0]['Zip/Postal code'])

    phone_input = context.driver.find_element("xpath", "//input[@id='field-phone']")
    phone_input.send_keys(data[0]['Phone'])
    

@when('user clicks Save button')
def userClicksSaveButton(context):
    save_button = context.driver.find_element("xpath", "//button[@type='submit']")
    save_button.click()


@then(u'user is redirected to My address page')
def userIsRedirectedToMyaddressPage(context):
    yourAddresses_icon = context.driver.find_element("xpath", "//h1[normalize-space()='Your addresses']")
    assert yourAddresses_icon.is_displayed()


@when('close browser')
def closeBrowser(context):
    context.driver.close()








