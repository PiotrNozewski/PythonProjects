Feature: TC6 Contact Us Form

  Scenario: TC6 13 steps one by one
    Given browser is open
    When user is on login page
    Then user is redirected to Home page
    When user clicks on Contact Us button
    Then user is redirected to Get In Touch page
    When user fills up Name, Email, Subject, Message boxes
    When user is uploading file
    When user clicks Submit button
    When user clicks OK button
    Then user is informed by a PopUp whether his message was submitted
    When user clicks Home button
    When close browser
