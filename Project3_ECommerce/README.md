# SauceDemo E-Commerce Test Automation – Project 3

### 1. **Project Overview**

This project is an automated testing framework developed to validate the functional behavior of the SauceDemo e-commerce web application.
The framework is implemented using Python, Selenium WebDriver, Pytest, Pytest-BDD and Page Object Model (POM).
The project covers important e-commerce functionalities such as login, logout, product selection, cart operations, checkout and product sorting.

#### 2. **Application Under Test**

Application: SauceDemo

URL: https://www.saucedemo.com/

##### 3. **Testing Scope**

The following functionalities are covered in this project:

* Login functionality
* Positive login validation
* Negative login validation
* Logout functionality
* Product selection
* Add to Cart functionality
* Cart details validation
* Checkout functionality
* Product sorting
* Reset application state

##### 4.**Technologies Used**

Python	Programming language
Selenium WebDriver	Browser automation
Pytest-	Test execution framework
Pytest-BDD	BDD feature and step implementation
Page Object Model	Maintainable page structure
Excel -	Test data management
Allure -Test reporting
HTML Report	Test execution reporting
Chrome WebDriver -Browser execution

##### 5. Framework Design

This project follows the Page Object Model (POM) design pattern.
The application pages are represented using separate Page Object classes, while the test scenarios are written using Gherkin feature files and implemented through pytest-bdd step definitions.
The framework also uses reusable methods from the Base Page for common Selenium operations.

##### 6. Project Structure

Project3_ECommerce/
│
├── features/
│   ├── Login.feature
│   ├── Cart_Functionality.feature
│   ├── Checkout.feature
│   └── ...
│
├── step_defs/
│   ├── login_steps.py
│   ├── cart_steps.py
│   ├── checkout_steps.py
│   └── ...
│
├── pages/
│   ├── basepage.py
│   ├── loginpage.py
│   ├── homepage.py
│   ├── checkoutpage.py
│   └── ...
│
├── utils/
│   ├── excel_utility.py
│   └── ...
│
├── test_data/
│   └── test_data_file.xlsx
│
├── reports/
│
├── screenshots/
│
├── pytest.ini
├── requirements.txt
└── README.md


##### 7. Page Object Model

The framework uses Page Object Model to separate page locators and page actions from test step definitions.

Main Page Objects
Basepage
LoginPage
HomePage
CheckoutPage

The Basepage contains reusable Selenium operations such as:

1. Enter text
2. Click elements
3. Get text
4. Get current URL
5. Launch URL
6. Wait for elements
7. Close browser

##### 8. Test Data Management

Test data is maintained separately from the test scripts using an Excel file.
Example test data sheet:
Valid_Credential
The Excel utility is used to read the required test data during test execution.
This helps keep test data separate from the automation code.

##### 9. Login Testing

The login functionality includes both positive and negative scenarios.
Login Page Locators
The following locators were used:

Username     → id=user-name
Password     → id=password
Login Button → id=login-button
Error        → //h3[@data-test='error']
Positive Login

Valid credentials are entered and the user is expected to navigate to:

/inventory.html
Negative Login

Invalid login credentials are used to verify that the appropriate login error message is displayed.

##### 10. Cart Functionality

The cart module validates adding products to the shopping cart.
The automation identifies the available product cards and selects products for adding to the cart.
* The framework also captures:
* Selected product names
* Selected product prices
* Number of products added
* Cart badge count
* Cart product names
* Cart product prices

Example validation/debug information:

Number of products found
Selected product names
Selected product prices
Cart badge count
Number of cart products
Cart product names
Cart product prices

##### 11. Checkout Functionality

The checkout module automates the checkout flow after products are added to the cart.
The checkout page is handled using a dedicated Page Object class.
The test validates the required checkout interactions before completing the purchase flow.

##### 12. Product Sorting

The project also includes validation of SauceDemo's product sorting functionality.
The sorting options are used to verify the ordering of products based on the selected sorting criteria.

##### 13. Reset Functionality

The project includes validation of the Reset App State functionality available in SauceDemo.
This is used to reset the application state after performing cart-related operations.

##### 14. Pytest Markers

The project uses pytest markers to execute specific groups of tests.
The configured markers include:

login
logout
cart
productselection
cart_details
checkout
sorting
reset

Examples:

pytest -m login -v -s
pytest -m cart -v -s
pytest -m checkout -v -s
pytest -m sorting -v -s

##### 15. Installing the Project

Step 1 – Clone or download the project
Open the project in PyCharm.
Step 2 – Create a virtual environment
python -m venv .venv
Step 3 – Activate the virtual environment
For Windows PowerShell:
.venv\Scripts\Activate.ps1
Step 4 – Install dependencies
pip install -r requirements.txt

##### 16. Executing the Tests

Run all tests
pytest
Run with verbose output
pytest -v
Run with print/debug output
pytest -s
Run a specific module
pytest -m login -v -s
pytest -m cart -v -s
pytest -m checkout -v -s
pytest -m sorting -v -s

##### 17. Explicit Waits

The framework uses Selenium explicit waits to synchronize test execution with the application.
Example:
WebDriverWait(
    self.driver,
    timeout=20,
    poll_frequency=2
)
This helps avoid unnecessary hard-coded delays and improves test stability.

##### 18. Reporting

The project supports test execution reporting using:

HTML reports
Allure reports

###### HTML reports can be generated using:

pytest -m cart -v -s --html=report/tc7_report.html --self-contained-html
Allure results can be generated during execution and viewed using the Allure reporting tool.

##### 19. Screenshots

Screenshots are captured during selected test scenarios to help with debugging and test-result analysis.
The screenshots are stored in the project's screenshot/report-related directory.

##### 20. Key Automation Concepts Implemented

The following automation concepts were implemented in this project:
1. Selenium WebDriver
2. Python
3. Pytest
4. Pytest-BDD
5. Page Object Model
6. Reusable Base Page methods
7. Explicit waits
8. Excel-based test data
9. Positive and negative test scenarios
10. Pytest markers
11. HTML reporting
12. Allure reporting
13. Screenshot capture
14. E-commerce workflow automation

##### 21. Advantages of the Framework

The framework provides:
Reusable page methods
Separation of test logic and page locators
Maintainable test scripts
External test data management
Selective test execution using pytest markers
Reporting support
Easier debugging using screenshots and console output

##### 22. Conclusion

This project demonstrates the automation of important functional workflows of the SauceDemo e-commerce application using Selenium WebDriver with Python.
The combination of Pytest-BDD, Page Object Model, reusable page methods, Excel-based test data, explicit waits and reporting provides a structured and maintainable automation framework.

QA Automation Testing Project
Using Technologies: Python | Selenium | Pytest | Pytest-BDD | POM | Excel | Allure