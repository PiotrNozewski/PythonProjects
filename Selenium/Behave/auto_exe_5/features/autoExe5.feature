Feature: TC5 Register User with existing email

  Scenario: TC5 8 steps one by one
    Given browser is open
    When user is on login page
    Then user is redirected to Home page
    When user clicks Signup/Login button
    Then user is redirected to Login/Signup page
    When user fills up Name and Email Address box that already exist
    When user clicks Signup button
    Then user sees PopUp error about Email Address already exist
    When close browser

