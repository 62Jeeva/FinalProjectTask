import time

from pytest_bdd import given,when,then,scenarios
from selenium.webdriver.common.by import By

from pages.adminpage import AdminPage
from pages.homepage import HomePage
from pages.leavepage import LeavePage
from pages.loginpage import LoginPage
from pages.basepage import Basepage
from utils.excel_utility import ExcelUtility
from pages.myinfopage import MyInfoPage
from pages.claimpage import ClaimPage

scenarios("../features/login.feature")

EXCEL_PATH = "C:\\Users\\ADMIN\\PycharmProjects\\PythonTaskProject2\\Project2Package\\test_data\\test_data_file.xlsx"

@given("user navigates to orangehrm page")
def user_navigates_orangehrm(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()

@when("user enter the credentials")
def user_enter_credentials(driver):
    login_page = LoginPage(driver)
    excel = ExcelUtility(EXCEL_PATH)
    login_data =  excel.get_all_data("Login_Data")
    print("\nEXCEL DATA:")
    for row in login_data:
        print(row)
    driver.login_data = login_data


@when("user click login")
def user_click_login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    for row in driver.login_data:
        username = row["Username"]
        password = row["Password"]
        expected_result = row["Expected Result"]
        print(f"testing user: {username} | Expected:{expected_result}")
        login_page.open_login_page()
        print("Current url:",login_page.get_current_url())
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        actual_url = login_page.get_current_url()
        if expected_result == "Valid":
            assert "dashboard" in actual_url,f"Valid login failed for user: {username}"
            login_page.wait_for_dashboard()
            login_page.take_screenshot("tc_01_valid")
            home_page.logout()

        elif expected_result == "Invalid":
            assert "auth/login" in actual_url,f"Invalid login failed for user: {username}"
            login_page.invalid_error_message()
            login_page.take_screenshot("tc_01_invalid")



@given("user opens the browser")
def user_open_browser(driver):
    assert driver is not None

@then("user verifies the username and password field")
def verify_login_fields(driver):
    login_page = LoginPage(driver)

    assert login_page.is_username_displayed(),"Username field is not displayed"
    assert login_page.is_password_displayed(),"Password field is not displayed"

@given("user logs in with valid credentials")
def user_logs_in_with_valid_credentials(driver):
    excel = ExcelUtility(EXCEL_PATH)
    login_data = excel.get_all_data("Login_Data")
    row = login_data[0]
    username =  row["Username"]
    password = row["Password"]
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()


@then("user verifies the visibility and clickability of menu items")
def verify_menu_items(driver):
    home_page = HomePage(driver)
    home_page.verify_menu_items()

@then("user clicks each menu item")
def user_clicks_each_menu_item(driver):
    home_page = HomePage(driver)
    home_page.click_each_menu_item()

@given("user clicks admin menu item")
def user_clicks_admin_menu_items(driver):
    home_page = HomePage(driver)
    home_page.click_admin()

@given("clicks add icon")
def user_clicks_add_icon(driver):
    admin_page = AdminPage(driver)
    admin_page.click_add()

@then("user enters the required details and clicks save")
def user_enters_required_details_and_clicks_save(driver):
    excel = ExcelUtility(EXCEL_PATH)
    new_user_data = excel.get_all_data("New_User")
    row = new_user_data[0]
    employee_name = row["Employee Name"]
    username = row["Username"]
    password = row["Password"]
    confirm_password = row["Confirm password"]
    admin_page = AdminPage(driver)
    leave_page = LeavePage(driver)

#user role selection from dropdown
    admin_page.click_user_role_dropdown()
    admin_page.select_admin_role()

#employee name
    admin_page.enter_employee_name(employee_name)
    admin_page.select_employee_name(employee_name)

#selection of status
    admin_page.select_enabled_status()

#entering user credentials
    admin_page.enter_username(username)
    admin_page.enter_password(password)
    admin_page.enter_confirm_password(confirm_password)

#save
    admin_page.click_save()
    admin_page.take_screenshot("tc5_NewUser_record")


@then("user logs out")
def user_logs_out(driver):
    home_page = HomePage(driver)
    home_page.logout()

@then("user logs in with the newly created user")
def user_logs_in_with_newly_created_user(driver):
    excel = ExcelUtility(EXCEL_PATH)
    new_user_data = excel.get_all_data("New_User")
    row = new_user_data[0]
    username = row["Username"]
    password = row["Password"]
    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

@then("user verifies the created user")
def user_verifies_created_user(driver):
    excel = ExcelUtility(EXCEL_PATH)
    new_user_data = excel.get_all_data("New_User")
    row = new_user_data[0]
    username = row["Username"]
    admin_page = AdminPage(driver)
    admin_page.enter_search_username(username)
    admin_page.click_search()
    admin_page.scroll_to_record()
    admin_page.take_screenshot("tc_06")

@then("user clicks Forgot your password")
def user_clicks_forgot_password(driver):
    login_page = LoginPage(driver)
    login_page.click_forgot_password()

@then("user enters username")
def user_enters_username(driver):
    excel = ExcelUtility(EXCEL_PATH)
    forgot_password_data = excel.get_all_data("Forgot_password")
    row = forgot_password_data[0]
    username = row["Username"]
    login_page = LoginPage(driver)
    login_page.enter_reset_username(username)

@then("user clicks reset password")
def user_clicks_reset_password(driver):
    login_page = LoginPage(driver)
    login_page.click_reset_password()

@then("user clicks the My Info item and verifies the visibility of sub menu items")
def verify_myinfo_submenu_items(driver):
    home_page = HomePage(driver)
    my_info_page = MyInfoPage(driver)
    #clicking My Info
    home_page.click_my_info()
    #verifying all submenu items are visible and clickable
    my_info_page.verify_sub_menu_items()

@then("user clicks each sub menu item and landed on corresponding page")
def verify_each_myinfo_submenu_page(driver):
    home_page = HomePage(driver)
    my_info_page = MyInfoPage(driver)
    submenu_items = [
        (my_info_page.click_contact_details,"contactDetails"),
        (my_info_page.click_emergency,"viewEmergencyContacts"),
        (my_info_page.click_dependents, "viewDependents"),
        (my_info_page.click_immigration, "viewImmigration"),
        (my_info_page.click_job, "viewJobDetails"),
        (my_info_page.click_salary, "viewSalaryList"),
        (my_info_page.click_report_to, "viewReportToDetails"),
        (my_info_page.click_qualifications, "viewQualifications"),
        (my_info_page.click_memberships, "viewMemberships")

    ]
    for click_method,expected_url in submenu_items:
        #clicking submenu item
        click_method()
        #verifies the respective page url
        actual_url = my_info_page.get_current_url()
        assert expected_url in actual_url, f"Expected '{expected_url}' in URL , but got: {actual_url}"

@then("user clicks leave menu item and navigated to leave page")
def user_clicks_leave_menu_item(driver):
    home_page = HomePage(driver)
    home_page.click_leave()

@then("user clicks Assign leave tab")
def user_clicks_leave_tab(driver):
    leave_page = LeavePage(driver)
    leave_page.click_assign_leave()

@then("user enters the required details and clicks assign")
def user_enters_leave_details_and_clicks_assign(driver):
    excel = ExcelUtility(EXCEL_PATH)
    leave_data = excel.get_all_data("Leave_Data")
    row = leave_data[0]
    employee_name = row["Employee Name"]
    leave_type = row["Leave Type"]
    from_date = row["From Date"]
    to_date = row["To Date"]
    comments = row["Comments"]
    leave_page = LeavePage(driver)
    leave_page.enter_employee_name(employee_name)
    leave_page.select_employee_name(employee_name)
    leave_page.click_leave_type()
    leave_page.enter_from_date("2026-10-10")
    leave_page.enter_to_date("2026-12-10")
    leave_page.enter_comments(comments)
    leave_page.click_assignment_leave()
    leave_page.take_screenshot("tc9_leave2_record")

@then("user verifies the applied leave in Myleave record")
def user_verified_applied_leave(driver):
    leave_page = LeavePage(driver)
    leave_page.click_my_leave()
    print("checked")

@then("user clicks Claim option and landed on claim page")
def navigate_to_claim_page(driver):
    claim_page = ClaimPage(driver)
    claim_page.click_claim()

@then("user clicks submit claim option and enters the required details")
def submit_claim_request(driver):
    claim_page = ClaimPage(driver)
    claim_page.click_submit_claim()
    claim_page.click_event_dropdown()
    claim_page.click_currency_dropdown()
    claim_page.enter_remarks("Initiating claim for accommodation")

@then("user clicks create button")
def create_claim(driver):
    claim_page = ClaimPage(driver)
    claim_page.click_create()

@then("user verifies the initiated claim under My claims")
def verify_claim_under_my_claims(driver):
    claim_page = ClaimPage(driver)
    claim_page.click_my_claims()
    claim_page.scroll_to_record()
    claim_page.take_screenshot("tc_10")
    print("Claim has been initiated")




