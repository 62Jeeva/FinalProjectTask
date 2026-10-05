Feature:Verifying the login functionality

#TestCase1- Login with Predefined multiple-Users
@login
  Scenario:Verify different users are able to login
   Given user should be able to land on login page for login validation
    When user enters credentials and clicks login button  
    Then validate the login behavior


#TestCase2- Login with invalid credentials
@invalid
  Scenario:Verifying login page with invalid credentials
    Given user should be able to land on login page
    When user enters the invalid credentials and clicks login button
    Then validate the login behavior