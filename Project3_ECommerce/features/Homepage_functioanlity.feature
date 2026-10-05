Feature:Verifying Homepage Functionality

#TestCase3- Logout functionality
@logout
  Scenario:Verify user is able to logout
    Given user should be able to land on login page
    When user logs in with valid credentials
    Then validate the login behavior
    Then user clicks logout button


#TestCase4- CART Icon Visibility
@carticon
  Scenario:Verify cart icon is displayed
    Given user should be able to land on login page
    When user logs in with valid credentials
    Then validate the login behavior
    And verify the cart icon is displayed


#TestCase5- Random selection of products and data extraction
@productselection
  Scenario: Verify user able to select random products
    Given user should be able to land on login page
    When user logs in with valid credentials
    Then user able to select 4 products randomly and fetch their names and prices



