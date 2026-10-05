Feature:ORANGEHRM Validation

#Testcase1-Validating login using various credentials
@login
  Scenario: Validate the login functionality using multiple set of credentials
    Given user navigates to orangehrm page
    When user enter the credentials
    And user click login


#Testcase2- URL is accessible
@validurl

    Scenario: Validating the URL is accessible
      Given user opens the browser
      And user navigates to orangehrm page

#Testcase3- Validating login fields
@loginfields
     Scenario: Validating the visibility of username and password field
      Given user opens the browser
      And user navigates to orangehrm page
      Then user verifies the username and password field

#Testcase4 - verifying main menu items
@menu
     Scenario: Verifying the visibility and clickability of main menu items after login
      Given user opens the browser
      And user navigates to orangehrm page
      And user logs in with valid credentials
      Then user verifies the visibility and clickability of menu items
      And user clicks each menu item

#Testcase5 - creating new user and validating login
@newuser
    Scenario: Create a new user and validate login
    Given user navigates to orangehrm page
    And user logs in with valid credentials
    And user clicks admin menu item
    And clicks add icon
    Then user enters the required details and clicks save
    And user logs out
    And user logs in with the newly created user

#Testcase 6-validating new user in admin user list
@userlist
    Scenario: Validate presence of the newly created user in the admin user list
    Given user navigates to orangehrm page
    And user logs in with valid credentials
    And user clicks admin menu item
    Then user verifies the created user

#Testcase 7 -Verifying the Forgot password
@forgotpassword
    Scenario: Verify Forgot Password link functionality
      Given user navigates to orangehrm page
      Then user clicks Forgot your password
      And user enters username
      Then user clicks reset password

#Testcase8 -Validating presence of menu items under My info
@myinfo
   Scenario: Validate the presence of menu items under My info
    Given user navigates to orangehrm page
    And user logs in with valid credentials
    Then user clicks the My Info item and verifies the visibility of sub menu items
    And  user clicks each sub menu item and landed on corresponding page


#Testcase 9- Assigning leave and verify assignment
@leave
  Scenario: Assign leave to an employee and verify assignment
    Given user navigates to orangehrm page
    And user logs in with valid credentials
    Then user clicks leave menu item and navigated to leave page
    And user clicks Assign leave tab
    And user enters the required details and clicks assign
    Then user verifies the applied leave in Myleave record

#Testcase10-Initiate a claim request

@claimrequest
    Scenario: Initiating the claim request
    Given user navigates to orangehrm page
    And user logs in with valid credentials
    Then user clicks Claim option and landed on claim page
    And user clicks submit claim option and enters the required details
    Then user clicks create button
    And user verifies the initiated claim under My claims
