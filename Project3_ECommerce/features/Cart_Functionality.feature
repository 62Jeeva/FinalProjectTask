Feature:Verifying the Cart functionality

#TestCase6-Adding selected products from cart
@cart
  Scenario: Adding selected products to the cart and validating
    Given user should be able to land on login page
    When user logs in with valid credentials
    Then user able to select 4 products randomly and add them to cart
    And verify cart item count is 4
    And user clicks on cart icon and navigate to the cart page
    And Verify the selected products are listed in the cart


#Testcase 7-Validating product items in the cart
@cart_details
  Scenario: Validate product details inside the cart
    Given user should be able to land on login page
    When user logs in with valid credentials
    Then validate the login behavior
    And add products to the cart
    And user clicks on cart icon and navigate to the cart page
    Then verify the product details in the cart



#Testcase 8 -Complete checkout and validate order

@checkout
 Scenario: Validating the checkout process in Cart
    Given user should be able to land on login page
    When user logs in with valid credentials
    And add products to the cart
    And user clicks on cart icon and navigate to the cart page
    Then verify the product details in the cart
    Then user clicks checkout button and navigate to customer information page
    And user enter firstname lastname and Postal code
    And user clicks on continue button and lands on the checkout overview page
    And user clicks finish button and lands on order completion page
    Then verify the order confirmation page

#Testcase 9: Validating the sorting sorting behaviour
@sorting
  Scenario: Validating the sorting functionality
    Given user should be able to land on login page
    When user logs in with valid credentials
    Then user click sorting dropdown and select price low to high option
    And verify the products sorted based on low to high
    Then selects the sorting option Z to A order
    And verify the products are sorted in Z to A order



#Testcase 10: Reset App state

@reset
  Scenario: Validating the reset app state post selection of products
    Given user should be able to land on login page
    When user logs in with valid credentials
    And add products to the cart
    And user clicks on cart icon and navigate to the cart page
    Then user clicks on menu icon on the top left corner
    And user selects the Reset App state option
    Then verify the cart is empty



