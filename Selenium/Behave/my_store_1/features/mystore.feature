Feature: MyStore Feature

  Scenario: MyStore Step By Step
    Given browser is open
    When user is on login page
    When user clicks on Sign in button
    When user fills up email and password box
    When user clicks SIGN IN button
    Then user is redirected to Your account page
    When user clicks ADDRESSES button
    When user clicks PlusCreateNewAddress button
    When user fills up New address form
      | Alias   | Company     | VAT number | Address      | Address Complement | City       | Zip/Postal code | Phone     |
      | Piotrek | Power China | 1080013725 | Imagined One | 16/3               | Wonderland | 93-69Y          | 123456789 |
    When user clicks Save button
    Then user is redirected to My address page
    And close browser


