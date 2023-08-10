Feature: TC2 Login User with correct email and password

  Scenario: TC2 Login user with correct email and password Step By Step
    Given browser is open
    When user is on login page
    Then user is redirected to Home page
    When user clicks Signup/Login button
    Then user is redirected to Login/Signup page
    When user fills up Email Address and Password box
    When user clicks Login button
    Then user is redirected to Home page as logged user
    When user clicks Delete Account button
    Then user is redirected to Account Deleted page
    When close browser
