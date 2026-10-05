from pytest_bdd import given,when,then,scenarios
from selenium.common import NoAlertPresentException
from selenium.webdriver.firefox import webdriver

from selenium import webdriver
from pages.loginpage import LoginPage
from utils.excel_utility import read_login_data

scenarios("../features/Login_Functionality.feature")

SAUCEDEMO_URL = "https://www.saucedemo.com"


@given("user should be able to land on login page for login validation")
def user_lands_on_login_page():
    print("User will ready to validate login credentials")

@when("user enters credentials and clicks login button")
def user_enter_credentials(login_results):
    login_data = read_login_data("C:/Users/ADMIN/PycharmProjects/PythonProject2/Project3_ECommerce/test_data/Test_Data_file.xlsx","Valid_Credential")
    #home_page = HomePage(driver)
    for row in login_data:
        tc_id = row[0]
        username = row[1]
        password = row[2]
        expected_result = row[3]
        driver = webdriver.Chrome()

        try:
            login_page = LoginPage(driver)
            login_page.launch_url(SAUCEDEMO_URL)
            print(f"{tc_id} Username = [{username}]")
            print(f"{tc_id} Password = [{password}]")
            login_page.enter_username(username)
            login_page.enter_password(password)
            login_page.click_login()

            if login_page.is_login_successful():
                actual_result = "Login Successful"
            else:
                actual_result = "Login Failed"

                if login_page.is_error_displayed():
                    print(f"{tc_id}: Error displayed:{login_page.get_error_message()}")
            print(f"{tc_id}URL after wait:{driver.current_url}")

            login_results.append((tc_id,expected_result,actual_result))
            print(f"{tc_id}:Expected = {expected_result}; Actual = {actual_result}")

        finally:
            driver.quit()

@then("validate the login behavior")
def validating_login(login_results):
    for result in login_results:
        tc_id =  result[0]
        expected_result = result[1]
        actual_result = result[2]

        assert expected_result == actual_result,(f"{tc_id} failed." f"Expected: {expected_result}; Actual: {actual_result}")

#Step-defs for TestCase 2: Login with invalid credentials
@given("user should be able to land on login page")
def user_lands_on_login_page(driver):
    login_page = LoginPage(driver)
    login_page.launch_url(SAUCEDEMO_URL)

@when("user enters the invalid credentials and clicks login button")
def validating_with_invalid_details(driver,login_results):
    login_data = read_login_data("C:/Users/ADMIN/PycharmProjects/PythonProject2/Project3_ECommerce/test_data/Test_Data_file.xlsx","Invalid_Credential")
    login_page = LoginPage(driver)
    #home_page = HomePage(driver)
    for row in login_data:
        tc_id = row[0]
        username = row[1]
        password = row[2]
        expected_result = row[3]
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        if driver.current_url.startswith("https://www.saucedemo.com"):
            actual_result = "Login Failed"
        else:
            actual_result = "Login Successful"

        login_results.append((tc_id,expected_result,actual_result))
        print(f"{tc_id}:Expected = {expected_result}; Actual = {actual_result}")

        login_page.launch_url(SAUCEDEMO_URL)