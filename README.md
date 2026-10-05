# OrangeHRM Test Automation Framework – Project 2

##### 1. Project Overview

This project is a web automation testing framework developed to automate functional test scenarios for the OrangeHRM web application.
The framework is implemented using Python, Selenium WebDriver, Pytest, Pytest-BDD and Page Object Model (POM).
The project covers multiple OrangeHRM modules including login, menu navigation, user management, forgot password, My Info, Leave and Claim functionality.
The framework also uses Excel-based test data, explicit waits, screenshots and test reporting.

##### 2. Application Under Test

Application: OrangeHRM
URL:
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

##### 3. Testing Scope

The following functional areas were automated and validated as part of this project:
* 
* Login functionality
* Login field validation
* URL validation
* Menu navigation
* New User creation
* User List
* Forgot Password
* My Info
* Leave Assignment
* Claim Request

##### 4. Technologies Used

Technology - Purpose

1. Python	-Programming language
2. Selenium WebDriver-	Web browser automation
3. Pytest	-Test execution framework
4. Pytest-BDD-	Behavior Driven Development
5. Page Object Model-	Page and locator management
6. Excel-	External test data management
7. Allure	-Test reporting
8. Pytest HTML	-HTML test reporting
9. Chrome WebDriver-	Browser automation

##### 5. Framework Design

The project follows the Page Object Model (POM) design pattern.

The framework separates:
Page locators
Page actions
Feature files
Step definitions
Test data
Utility functions
Test configuration

The project uses Pytest-BDD to define test scenarios in Gherkin format and implement the scenarios using Python step definitions.

##### 6. Project Structure

Project2Package/
│
├── features/
│   ├── Login.feature
│
├── step_defs/
│   ├── test_step.py
│
├── pages/
│   ├── basepage.py
│   ├── loginpage.py
│   ├── homepage.py
│   ├── myinfopage.py
│   ├── leavepage.py
│   ├── claimpage.py
│   └── adminpage.py
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
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

##### 7. Page Object Model

The framework uses Page Object Model to maintain page-specific locators and actions separately from the test scenarios.
A reusable Basepage is used for common Selenium operations.
Common Base Page Operations
Launch URL
Enter text
Click elements
Get text
Get current URL
Wait for elements
Close browser
Screenshot capture
Using a common base class reduces duplicate Selenium code across different page classes.

##### 8. Test Data Management

Test data is maintained separately from the automation scripts using an Excel workbook.
The project uses:

test_data/test_data_file.xlsx
The workbook contains data sheets used by different test scenarios.
Examples include:
Login_Data
New_User
Forgot_password
Leave_Data

The Excel utility is used to read the required test data during execution.
Separating test data from the automation code makes the framework easier to maintain and update.

##### 9. Login Functionality

The login module validates the OrangeHRM authentication functionality.
The test scenarios cover login-related validations using valid and invalid credentials.
The login page is accessed using:

https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Login test data is maintained in the Excel workbook under:
Login_Data

##### 10. URL Validation

The project validates the expected OrangeHRM application URL.
URL validation helps confirm that the application is launched at the expected location before continuing with further interactions.

##### 11. Login Field Validation

The login module also validates the login page fields and their behavior.
The automation checks the required login page elements and performs the appropriate user interactions.

##### 12. Menu Navigation

The project validates navigation through different OrangeHRM menu options.
The menu scenarios verify that the required menu options can be accessed and that the corresponding pages are loaded.
This provides basic functional validation of the application's navigation structure.

##### 13. New User Creation

The New User module automates the process of creating a new system user.
The automation interacts with the required fields, including employee and user-related information.
Test data is maintained externally in the Excel workbook.
The scenario also covers navigation to the user management functionality.

##### 14. User List

The User List functionality is automated to validate access to the list of users.
The test interacts with the user list page and performs the required search/list operations.
This scenario helps validate the user management functionality of OrangeHRM.

##### 15. Forgot Password

The Forgot Password functionality is automated to validate navigation to the password reset page and submission of the required username information.
The test data is maintained in the:
Forgot_password Excel sheet.

##### 16. My Info

The My Info module is automated to validate access to employee information sections.
The automation covers navigation through areas such as:
* Personal Details
* Contact Details
* Emergency Contacts
* Dependents
* Immigration
* Job Details
* Salary
* Report To
* Qualifications
* Memberships

The test verifies navigation to the respective My Info sections.

##### 17. Leave Assignment

The Leave module automates the process of assigning leave to an employee.
The scenario includes:
1. Navigating to Leave
2. Selecting an employee
3. Selecting Leave Type
4. Entering From Date
5. Entering To Date
6. Assigning the leave

The employee information and leave data are maintained using the Excel test data.
The automation uses the appropriate date fields and validates the interaction with the leave form.
Confirmation Dialog
During leave assignment, OrangeHRM may display a confirmation dialog when the employee does not have sufficient leave balance.
The automation handles the confirmation dialog and selects the OK option to continue with the assignment.

##### 18. Claim Request

The Claim module automates the claim submission workflow.
The scenario includes:
* Navigating to Claim
* Selecting Submit Claim
* Selecting Event
* Selecting Currency
* Entering Remarks
* Creating the claim
* Navigating to My Claims

The Event and Currency dropdowns are handled using the actual OrangeHRM dropdown elements.
Example Event selection:
Accommodation
The Currency dropdown is opened and the required currency option is selected.
Remarks are entered before submitting the claim.

##### 19. Pytest-BDD

The project uses Pytest-BDD for Behavior Driven Development.
The test scenarios are written using Gherkin syntax.
Common BDD keywords include:

Feature
Scenario
Given
When
Then

The corresponding steps are implemented using Python step-definition files.
This makes the test scenarios easier to understand and maintain.

##### 20. Pytest Markers

Pytest markers are configured in pytest.ini to allow individual test modules to be executed separately.
The project uses markers including:

login
validurl
loginfields
menu
newuser
userlist
forgotpassword
myinfo
leave
claimrequest

Examples
Run Login tests:
pytest -m login -v -s
Run New User tests:
pytest -m newuser -v -s
Run Leave tests:
pytest -m leave -v -s
Run Claim Request tests:
pytest -m claimrequest -v -s

##### 21. How to Install the Project

Step 1 – Open the project
Open Project2Package in PyCharm.
Step 2 – Create a virtual environment
python -m venv .venv
Step 3 – Activate the virtual environment
For Windows PowerShell:
.venv\Scripts\Activate.ps1
Step 4 – Install dependencies
pip install -r requirements.txt

##### 22. How to Execute Tests

Run all tests
pytest
Run tests with verbose output
pytest -v
Run tests with console output
pytest -s
Run a specific module
pytest -m login -v -s
pytest -m newuser -v -s
pytest -m userlist -v -s
pytest -m forgotpassword -v -s
pytest -m myinfo -v -s
pytest -m leave -v -s
pytest -m claimrequest -v -s

##### 23. Explicit Waits

The framework uses Selenium explicit waits for synchronizing interactions with dynamic web elements.
The Base Page uses WebDriverWait with a defined timeout and polling interval.
Example:

WebDriverWait(
    self.driver,
    timeout=20,
    poll_frequency=2
)
Explicit waits are preferred over unnecessary hard-coded delays because they allow the automation to wait for the required condition before interacting with an element.

##### 24. Screenshots

The framework includes screenshot capture for test scenarios.
Screenshots are useful for:
Debugging failures
Investigating unexpected application behavior
Maintaining execution evidence
Reviewing test execution results

Screenshots are stored in the project's screenshot-related directory.

##### 25. HTML Reporting

The project supports HTML test reporting using the pytest HTML reporting plugin.
Example:
pytest -m leave -v -s --html=report/tc09_report.html --self-contained-html
This generates a self-contained HTML report containing the test execution results.

##### 26. Allure Reporting

The project also supports Allure reporting.
Allure results can be generated during test execution and viewed using the Allure reporting tool.
This provides a more detailed and visually structured representation of test execution results.

##### 27. Key Automation Concepts Implemented

The following automation concepts were implemented in this project:
* Python
* Selenium WebDriver
* Pytest
* Pytest-BDD
* Page Object Model
* Gherkin feature files
* Step definitions
* Reusable Base Page
* Explicit waits
* Excel-based test data
* Pytest markers
* Positive and negative testing
* Dropdown handling
* Date field handling
* Autocomplete handling
* Confirmation dialog handling
* URL validation
* Navigation validation
* Screenshot capture
* HTML reporting
* Allure reporting

##### 28. Framework Benefits

The framework provides:

Reusable page methods
Separation of page locators and test logic
Maintainable Page Object Model structure
Readable BDD scenarios
External Excel test data
Selective test execution using pytest markers
Explicit wait implementation
Screenshot support
HTML reporting
Allure reporting
Easier debugging and maintainence

##### 29. Conclusion

This project demonstrates functional web application automation of the OrangeHRM application using Python, Selenium WebDriver, Pytest, Pytest-BDD and Page Object Model.
The project covers multiple functional modules and demonstrates practical automation techniques including dynamic dropdown handling, autocomplete selection, date field handling, confirmation dialog handling, external test data management, explicit waits and test reporting.
The framework provides a structured and maintainable approach for developing and executing Selenium automation test cases.

QA Automation Testing Project
Technologies Used: Python | Selenium | Pytest | Pytest-BDD | POM | Excel | Allure | HTML Reporting