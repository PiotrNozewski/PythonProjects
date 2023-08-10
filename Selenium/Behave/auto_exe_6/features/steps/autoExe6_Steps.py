from behave import *
from selenium import webdriver
from selenium.webdriver.common.alert import Alert


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


@when('user clicks on Contact Us button')
def userClicksOnContactUsButton(context):
    contact_us_button = context.driver.find_element("xpath", "//a[normalize-space()='Contact us']")
    contact_us_button.click()


@then('user is redirected to Get In Touch page')
def userIsRedirectedToGetInTouchPage(context):
    get_in_touch_icon = context.driver.find_element("xpath", "//h2[normalize-space()='Get In Touch']")
    assert get_in_touch_icon.is_displayed()


@when('user fills up Name, Email, Subject, Message boxes')
def userFillsUpNameEmailSubjectMessageBoxes(context):
    name_input = context.driver.find_element("xpath", "//input[@placeholder='Name']")
    name_input.click()
    name_input.send_keys("Piotr")

    email_input = context.driver.find_element("xpath", "//input[@placeholder='Email']")
    email_input.click()
    email_input.send_keys("pn@gmail.com")

    subject_input = context.driver.find_element("xpath", "//input[@placeholder='Subject']")
    subject_input.click()
    subject_input.send_keys("IDK")

    message_input = context.driver.find_element("xpath", "//textarea[@id='message']")
    message_input.click()
    message_input.send_keys("Hello, I'm contacting You because of...")


@when('user is uploading file')
def userIsUploadingFile(context):
    upload_file = context.driver.find_element("xpath", "//input[@name='upload_file']")
    upload_file.send_keys("C:\\Users\piotr\OneDrive\Pulpit\\autoExe.txt")


@when('user clicks Submit button')
def userClicksSubmitButton(context):
    submit_button = context.driver.find_element("xpath", "//input[@name='submit']")
    submit_button.click()


@when('user clicks OK button')
def userClicksOKButton(context):
    Alert(context.driver).accept()


@then('user is informed by a PopUp whether his message was submitted')
def userIsInformedByPopUpWhetherHisMessageWasSubmitted(context):
    message_submitted_popup = context.driver.find_element("xpath", "//div[@class='status alert alert-success']")
    assert message_submitted_popup.is_displayed()


@when('user clicks Home button')
def userClicksHomeButton(context):
    home_button = context.driver.find_element("xpath", "//a[contains(text(),'Home')]")
    home_button.click()


@when('close browser')
def closeBrowser(context):
    context.driver.close()
