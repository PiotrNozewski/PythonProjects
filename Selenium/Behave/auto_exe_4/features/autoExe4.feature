Feature: TC4 Logout User
  Scenario: TC4 10 steps one by one
    Given browser is open
    When user is on login page
    Then user is redirected to Home page
    When user clicks Signup/Login button
    Then user is redirected to Login/Signup page
    When user fills up Email Address and Password box
    When user clicks Login button
    Then user is redirected to Home page as logged user
    When user clicks Logout button
    Then user is redirected to Login page
    When close browser