# GUVI Website Test Automation – Project 1

##### 1.Project Overview

This project is a web automation testing framework developed to validate the functional behavior and basic navigation of the GUVI website.
The framework is implemented using Python, Selenium WebDriver, Pytest, Pytest-BDD and Page Object Model (POM).
The project focuses on validating important website elements, page navigation and basic user interactions.

##### 2. Application Under Test

Application: GUVI
URL: https://www.guvi.in/

##### 3. Testing Scope

The following functionalities and validations are covered in this project:

1. GUVI URL validation
2. Page title validation
3. Login button validation
4. Login page navigation
5. Signup navigation
6. Signup page URL validation
7. Basic website navigation
8. UI element validation

##### 4. Technologies Used

Technology-	Purpose
Python-	Programming language
Selenium WebDriver-	Web browser automation
Pytest-	Test execution framework
Pytest-BDD	Behavior Driven Development
Page Object Model-	Page and locator management
Excel-	Test data management
Allure-	Test reporting
HTML Report-	Test execution reporting
Chrome WebDriver-	Browser automation

##### 5.Framework Design

The project follows the Page Object Model (POM) design pattern.
Page-specific locators and actions are maintained separately from the test step definitions.
The test scenarios are written using Gherkin feature files, while the corresponding steps are implemented using pytest-bdd step definitions.
This approach improves readability, reusability and maintainability of the automation framework.

##### 6. Project Structure

Project1Package/
│
├── features/
│   └── login.feature
│
├── step_defs/
│   └── test_step.py
│
├── pages/
│   ├── basepage.py
│   └── loginpage.py
│
├── utils/
│   └── *.py
│
├── reports/
│
├── pytest.ini
├── requirements.txt
└── README.md

The exact file names may vary depending on the final project structure.

##### 7. Page Object Model

The project uses Page Object Model to separate page locators and page actions from test scenarios.
The Base Page contains reusable Selenium operations that can be used by different page classes.
Common reusable operations include:

1. Launch URL
2. Click element
3. Enter text
4. Get text
5. Get current URL
6. Wait for elements
7. Close browser

##### 8. GUVI URL Validation

The GUVI home page URL is validated using Selenium.

Expected URL:
https://www.guvi.in/
The URL validation scenario verifies that the application loads the expected GUVI website.

##### 9. Page Title Validation

The project validates the expected title of the GUVI home page.
Expected title:
GUVI | Learn to code in your native language
The test verifies that the browser page title matches the expected application title.

##### 10. Login Button Validation

The project validates the presence and functionality of the Login button on the GUVI home page.
The Login button locator used during the automation was based on the actual DOM element.
The login navigation was validated to ensure that the user can access the GUVI sign-in page.

##### 11. Login Page Navigation
The expected GUVI sign-in page is:
https://www.guvi.in/sign-in/
The automation validates navigation from the GUVI home page to the sign-in page.

##### 12. Signup Navigation

The project validates navigation to the GUVI registration page.
Expected registration URL:

https://www.guvi.in/register/
The signup scenario verifies that the user is redirected to the expected registration page.

##### 13. Pytest-BDD

The project uses Pytest-BDD to implement Behavior Driven Development.
Test scenarios are written in Gherkin format using:

* Feature
* Scenario
* Given
* When
* Then

The corresponding step definitions are implemented using pytest-bdd decorators.
This provides a readable structure for describing application behavior.

##### 14. Pytest Markers

Pytest markers are used to execute specific test scenarios selectively.
Examples of markers used in the project include:
url
title
loginbutton
signup
A specific marked test can be executed using:
pytest -m url -v
The -v option provides verbose test execution information.

##### 15. How to Install the Project

Step 1 – Open the project
Open Project1Package in PyCharm.
Step 2 – Create a virtual environment
python -m venv .venv
Step 3 – Activate the virtual environment
For Windows PowerShell:
.venv\Scripts\Activate.ps1
Step 4 – Install project dependencies
pip install -r requirements.txt

##### 16. How to Execute Tests

Run all tests
pytest
Run tests with verbose output
pytest -v
Run a specific marked test
pytest -m url -v
Run tests with console output
pytest -m url -v -s

##### 17. Explicit Waits

The automation framework uses Selenium explicit waits to synchronize browser actions with web elements.
Explicit waits help the automation wait for elements to become available before performing actions.
This improves the reliability of the test execution compared with using unnecessary fixed delays.

##### 18. Test Reporting

The project is structured to support test reporting using:
* HTML reports
* Allure reports

HTML reports can be generated using the pytest HTML reporting plugin.
Example:
pytest -m url -v --html=report/url_report.html --self-contained-html
Allure results can also be generated during test execution and viewed using the Allure reporting tool.

##### 19. Key Automation Concepts Implemented

The project demonstrates the following automation concepts:
* Python
* Selenium WebDriver
* Pytest
* Pytest-BDD
* Page Object Model
* Gherkin feature files
* Step definitions
* Reusable page methods
* Explicit waits
* Pytest markers
* URL validation
* Page title validation
* UI element validation
* Navigation testing
* HTML reporting
* Allure reporting
* Screenshot capture

##### 20. Framework Benefits

The framework provides:

1. Separation of test scenarios and page implementation
2. Reusable Selenium methods
3. Maintainable page objects
4. Readable BDD scenarios
5. Selective test execution using pytest markers
6. Better debugging through reports and screenshots
7. Structured automation project organization

##### 21. Conclusion

This project demonstrates the automation of basic functional and navigation validations of the GUVI website using Selenium WebDriver with Python.
The use of Pytest-BDD, Page Object Model, reusable page methods, explicit waits and reporting provides a structured foundation for web application automation testing.
QA Automation Testing Project
Technologies Used: Python | Selenium | Pytest | Pytest-BDD | POM | Allure | HTML Reporting