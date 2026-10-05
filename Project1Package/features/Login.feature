Feature:Verifying GUVI page

#Testcase1 - verify Guvi URL is valid or not

@url
  Scenario: verify whether the given URL is valid or not
    Given user navigates to the GUVI website
    Then GUVI Webpage should load successfully

#Testcase2 - verify title
@title
  Scenario: Verify whether the title of the webpage is correct
    Given user navigates to the GUVI website
    Then user verifies the title as GUVI | Learn to code in your native language

#Testcase3 - verifying login button
@loginbutton
  Scenario: Verify the visibility and clickability of the Login button
    Given user navigates to the GUVI website
    Then GUVI Webpage should load successfully
    Then user verifies the login button is displayed
    And user clicks login button and navigates to login page

#Testcase4
@signup
  Scenario: Verify the visibility and clickability of sign-up button
    Given user navigates to the GUVI website
    Then GUVI Webpage should load successfully
    Then user verifies the sign-up button is displayed
    And user clicks the sign up button and navigates to register page


#Testcase5
@signin
  Scenario:Verify navigation to the register page via the sign-up button
    Given user navigates to the GUVI website
    When user clicks the sign up button
    Then user should be navigated to the register page

#Testcase6
@performlogin
  Scenario: verifying login functionality with valid credentials
    Given user navigates to the GUVI website
    When user clicks login button and navigates to login page
    Then user enters valid email and password and performs login
    And user should be logged in and redirected to the dashboard

#Testcase7
@invalidcredentials
  Scenario: Verify the login with invalid credentials
    Given user navigates to the GUVI website
    When user clicks login button and navigates to login page
    Then user enters invalid email and password and performs login
    And user verifies the error message

#Testcase8
@menu
  Scenario: verify that menu items like courses live classes and practice is displayed
    Given user navigates to the GUVI website
    And user validates the menu items Courses Live classes practice is displayed


#Testcase9
@dobby
  Scenario: Validate that the dobby Guvi Assistant is present on the page
    Given user navigates to the GUVI website
    When user clicks login button and navigates to login page
    Then user enters valid email and password and performs login
    And user validates the dobby assistant widget/chatbot

#Testcase 10
@logout
  Scenario: validate logout functionality
    Given user navigates to the GUVI website
    When user clicks login button and navigates to login page
    Then user enters valid email and password and performs login
    And user clicks the logout option
    And user should be logged out successfully

