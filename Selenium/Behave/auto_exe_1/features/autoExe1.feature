Feature: AE1 Register User

  Scenario: AE1 Register User Step By Step
    Given browser is open
    When user is on login page
    Then user is redirected to Home page
    When user clicks Signup/Login button
    Then user is redirected to Login/Signup page
    When user fills up Name and Email Address box
    When user clicks Signup button
    Then user is redirected to Enter Account Information page
    When user fills All The Data Needed To Proceed
    When user clicks Sign up for our newsletter button
    When user clicks Receive Special Offers From Our Partners button
    When user clicks Create Account button
    Then user is redirected to Account Created page
    When user clicks Continue button
    When user click Delete Account button
    Then user is redirected to Account Deleted page
    When close browser


