from pytest_bdd import given,when,then,scenarios

from Project1Package.pages.homepage import HomePage
from Project1Package.pages.loginpage import LoginPage
from Project1Package.pages.basepage import Basepage

scenarios("../features/login.feature")

@given("user navigates to the GUVI website")
def user_navigate_guvi(driver):
    login_page = LoginPage(driver)
    login_page.launch_url()

@then("GUVI Webpage should load successfully")
def guvi_loaded_successfully(driver):
    login_page = LoginPage(driver)
    actual_url = login_page.get_current_url()
    assert "guvi" in actual_url,"Webpage not loaded successfully"
    login_page.take_screenshot("tc_01")


@then("user verifies the title as GUVI | Learn to code in your native language")
def verify_title(driver):
    base_page = Basepage(driver)
    title = base_page.get_title()
    assert title == "HCL GUVI | Learn to code in your native language","Title mismatch"
    base_page.take_screenshot("tc_02")

@then("user verifies the login button is displayed")
def login_button_displayed(driver):
    login_page = LoginPage(driver)
    assert login_page.main_login_displayed(),"Login button not displayed"

@then("user clicks login button and navigates to login page")
def click_login_button(driver):
    login_page = LoginPage(driver)
    login_page.click_login_btn()
    actual_url = login_page.get_current_url()
    assert "https://www.guvi.in" in actual_url,"Login page open failed"
    login_page.take_screenshot("tc_03")

@then("user verifies the sign-up button is displayed")
def verify_signup_button(driver):
    login_page = LoginPage(driver)
    assert login_page.sign_up_displayed(),"Sign up button not displayed"

@then("user clicks the sign up button and navigates to register page")
def click_sign_up(driver):
    login_page = LoginPage(driver)
    login_page.click_sign_up()
    actual_url = login_page.get_current_url()
    assert "https://www.guvi.in/" in actual_url,"Page navigation failed"

@when("user clicks the sign up button")
def click_sign_up_button(driver):
    login_page = LoginPage(driver)
    login_page.click_sign_up()

@then("user should be navigated to the register page")
def click_register_button(driver):
    login_page = LoginPage(driver)
    try:
        actual_url = login_page.get_current_url()
        assert "https://www.guvi.in/" in actual_url,"User is not navigated to register page"
        login_page.take_screenshot("tc_05")

    except Exception as e:
        print("Register page navigation failed:",e)
        raise

@then("user enters valid email and password and performs login")
def login_valid_email_password(driver):
    login_page = LoginPage(driver)
    login_page.login("gvajk625@gmail.com","Jeeva@123")

@then("user should be logged in and redirected to the dashboard")
def verify_login_success(driver):
    home_page = HomePage(driver)
    assert home_page.verify_login(),"User is not logged in successfully"


@then("user enters invalid email and password and performs login")
def login_invalid_email_password(driver):
    login_page = LoginPage(driver)
    login_page.login("qwdqwdq@gma.com","21312jioqw")

@then("user verifies the error message")
def verify_error_message(driver):
    login_page = LoginPage(driver)
    error_message = login_page.invalid_email_password()
    assert error_message == "Incorrect Email or Password","Expected Error message was not displayed"
    login_page.take_screenshot("tc_07")

@given("user validates the menu items Courses Live classes practice is displayed")
def validate_menu_items(driver):
    home_page = HomePage(driver)
    base_page = Basepage(driver)
    assert home_page.validate_menu(),"Menu items are not displaying"
    base_page.take_screenshot("tc_08")


@then("user validates the dobby assistant widget/chatbot")
def validate_dobby_assistant_widget(driver):
    home_page = HomePage(driver)
    assert home_page.dobby_assistant(),"Dobby assistant widget is not displayed"
    login_page = LoginPage(driver)
    login_page.take_screenshot("tc_09")

@then("user clicks the logout option")
def click_logout(driver):
    home_page = HomePage(driver)
    home_page.logout()

@then("user should be logged out successfully")
def verify_logout_success(driver):
    login_page = LoginPage(driver)
    actual_url = login_page.get_current_url()
    assert "guvi.in" in actual_url,"User is not logged out successfully"
    login_page.take_screenshot("tc_10")
