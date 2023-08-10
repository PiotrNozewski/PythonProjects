Feature: TC3 Login User with incorrect email and password
  Scenario: TC3 Test Case 3: Login User with incorrect email and password Step By Step
    Given browser is open
    When user is on login page
    Then user is redirected to Home page
    When user clicks Signup/Login button
    Then user is redirected to Login/Signup page
    When user fills up Email Address and Password box with wrong details
    When user clicks Login button
    Then user gets PopUp about incorrect details
    When close browser