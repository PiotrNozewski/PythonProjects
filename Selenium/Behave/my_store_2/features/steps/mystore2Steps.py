from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select


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


@when('user clicks CLOTHES button')
def userClicksClothesButton(context):
    context.driver.get("https://prod-course.coderslab.com/index.php?id_category=3&controller=category")


@when('user clicks Hummingbird Printed Sweater item')
def userClicksHummingbirdPrintedSweaterItem(context):
    HPS_button = context.driver.find_element("xpath",
                                             "//div[@id='content-wrapper']//div[2]//article[1]//div[1]//div[1]//a[1]//img[1]")
    HPS_button.click()


@when('user checks 20% discount')
def userCHecksTwentyPercentDiscount(context):
    twentyPercent_icon = context.driver.find_element("xpath", "//span[@class='discount discount-percentage']")
    assert twentyPercent_icon.is_displayed()


@when('user chooses size M')
def userChoosesSizeM(context):
    size_dropdown = context.driver.find_element("id", "group_1")
    sizeM = Select(size_dropdown)
    sizeM.select_by_value("2")


@when('user takes five pieces of HPS item')
def userTakesFivePiecesOfHPSItem(context):
    quantity_button = context.driver.find_element("xpath", "//input[@id='quantity_wanted']")
    quantity_button.click()
    quantity_button.clear()
    quantity_button.send_keys("5")


@when('user clicks Add To Cart button')
def userClicksAddToCartButton(context):
    addToCart_button = context.driver.find_element("xpath", "//button[@class='btn btn-primary add-to-cart']")
    addToCart_button.click()


@when('user skips bugged window')
def userSkipsBuggedWindow(context):
    context.driver.get("https://prod-course.coderslab.com/index.php?controller=cart&action=show")


@when('user clicks Proceed To Checkout button')
def userClicksProceedToCheckoutButton(context):
    proceedToCheckout_button = context.driver.find_element("xpath", "//a[normalize-space()='Proceed to checkout']")
    proceedToCheckout_button.click()


@when('user clicks Continue button')
def userClicksContinueButton(context):
    continue_button = context.driver.find_element("xpath", "//button[@name='confirm-addresses']")
    continue_button.click()


@when('user clicks Self Pick Up button')
def userClicksSelfPickUpButton(context):
    selfPickUp_button = context.driver.find_element("xpath", "//div[@class='delivery-options']//div[1]//div[1]//span[1]//span[1]")
    selfPickUp_button.click()


@when('user clicks Continue (Shipping Method) button')
def userClicksContinueShippingMethodButton(context):
    continueSM_button = context.driver.find_element("xpath", "//button[@name='confirmDeliveryOption']")
    continueSM_button.click()


@when('user clicks Pay By Check button')
def userClicksPayByCheckButton(context):
    payByCheck_button = context.driver.find_element("xpath", "//input[@id='payment-option-1']")
    payByCheck_button.click()


@when('user clicks Terms Of Service button')
def userClicksTermsOfServiceButton(context):
    termsOfService_button = context.driver.find_element("xpath", "//input[contains(@id,'conditions_to_approve')]")
    termsOfService_button.click()


@when('user clicks Place Order button')
def userClicksPlaceOrderButton(context):
    placeOrder_button = context.driver.find_element("xpath", "//button[normalize-space()='Place order']")
    placeOrder_button.click()
