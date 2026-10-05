from pytest_bdd import given,when,then,scenarios
from selenium.webdriver.common.by import By

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utils.excel_utility import read_login_data
from pages.checkoutpage import CheckoutPage

scenarios("../features/Cart_Functionality.feature")

SAUCEDEMO_URL = "https://www.saucedemo.com/"


@given("user should be able to land on login page")
def user_lands_on_login_page(driver):
    login_page = LoginPage(driver)
    login_page.launch_url(SAUCEDEMO_URL)

@when("user logs in with valid credentials")
def user_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_data = read_login_data("C:/Users/ADMIN/PycharmProjects/PythonProject2/Project3_ECommerce/test_data/Test_Data_file.xlsx","Test_Login")
    row = login_data[0]
    username =  row[1]
    password = row[2]
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

@then("validate the login behavior")
def validating_login(driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

@then("user able to select 4 products randomly and add them to cart")
def select_random_products_and_add_to_cart(driver):
    home_page = HomePage(driver)
    selected_names,selected_prices = home_page.add_random_products_to_cart()


@then("verify cart item count is 4")
def verify_cart_item_count_is_4(driver):
    home_page = HomePage(driver)
    cart_count = home_page.get_cart_count()
    print("Cart item count:",cart_count)
    assert cart_count == "4"

@then("Verify the selected products are listed in the cart")
def verify_selected_products_are_list(driver):
    home_page = HomePage(driver)
    cart_product_names = home_page.get_cart_product_names()
    print("Selected products:",driver.selected_names)
    print("Cart products:",cart_product_names)
    assert cart_product_names == driver.selected_names


@when("add products to the cart")
def add_to_cart(driver):
    home_page = HomePage(driver)
    selected_names,selected_prices = home_page.add_random_products_to_cart()
    print("\nSelected products:")
    for name,price in zip(selected_names,selected_prices):
        print(f"Product Name: {name} | Price: {price}")

@when("user clicks on cart icon and navigate to the cart page")
def navigate_to_cart_page(driver):
    home_page = HomePage(driver)
    home_page.click_cart_icon()
    print("cart url:",driver.current_url)

@then("verify the product details in the cart")
def verify_product_details_in_cart(driver):
    home_page = HomePage(driver)
    cart_names = home_page.get_cart_product_names()
    cart_prices = home_page.get_cart_product_prices()
    selected_names = driver.selected_names
    selected_prices = driver.selected_prices
    print("Selected names:",selected_names)
    print("Cart names:",cart_names)
    print("Selected prices:",selected_prices)
    print("Cart prices:",cart_prices)
    assert cart_names ==selected_names,(f"Product names mismatch. " f"Expected:{selected_names}; Actual:{cart_names}")
    assert cart_prices == selected_prices,(f"Product prices mismatch. " f"Expected:{selected_prices}; Actual:{cart_prices}")
    print("\nCart product details are correct")


@then ("user clicks checkout button and navigate to customer information page")
def user_clicks_checkout_page(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_checkout()

@then("user enter firstname lastname and Postal code")
def enter_customer_details(driver):
    checkout_data = read_login_data("C:/Users/ADMIN/PycharmProjects/PythonProject2/Project3_ECommerce/test_data/Test_Data_file.xlsx","Checkout_UserDetails")
    checkout_page = CheckoutPage(driver)
    for row in checkout_data:
        firstname = row[1]
        lastname = row[2]
        postalcode = str(row[3])
        checkout_page.enter_customer_information(firstname,lastname,postalcode)

@then("user clicks on continue button and lands on the checkout overview page")
def click_continue_button(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_continue()

@then("user clicks finish button and lands on order completion page")
def click_finish_button(driver):
    checkout_page = CheckoutPage(driver)
    driver.save_screenshot("screenshots/order_summary.png")
    checkout_page.click_finish()
    driver.save_screenshot("screenshots/order_confirmation.png")

@then("verify the order confirmation page")
def verify_order_confirmation(driver):
    checkout_page = CheckoutPage(driver)
    actual_message = checkout_page.get_order_confirmation_message()
    expected_message = "Thank you for your order!"
    assert actual_message == expected_message
    print("Order confirmation:",actual_message)

@then("user click sorting dropdown and select price low to high option")
def select_price_low_to_high(driver):
    home_page = HomePage(driver)
    home_page.select_sort_option("Price (low to high)")

@then("verify the products sorted based on low to high")
def verify_price_low_to_high(driver):
    home_page = HomePage(driver)
    actual_prices =  home_page.get_product_prices()
    prices = [float(price.replace("$", "")) for price in actual_prices]
    assert prices == sorted(prices),f"Products are not sorted low to high. Actual prices:{prices}"
    print("\nProducts are sorted from low to high")
    print("Prices:",prices)

@then("selects the sorting option Z to A order")
def select_sort_option_Z_to_A_order(driver):
    home_page = HomePage(driver)
    home_page.select_sort_option("Name (Z to A)")

@then("verify the products are sorted in Z to A order")
def verify_name_z_to_a(driver):
    home_page = HomePage(driver)
    actual_names = home_page.get_product_names()
    expected_names = sorted(actual_names, reverse = True)
    assert actual_names == expected_names,f"Products are not sorted in Z to A. Actual names:{actual_names}"
    print("Products name:",actual_names)

@then("user clicks on menu icon on the top left corner")
def click_menu_icon(driver):
    home_page = HomePage(driver)
    home_page.click(home_page.MENU_ICON)

@then("user selects the Reset App state option")
def select_reset_app_state(driver):
    home_page = HomePage(driver)
    home_page.reset_app_state()

@then("verify the cart is empty")
def verify_cart_is_empty(driver):
    home_page = HomePage(driver)
    driver.save_screenshot("screenshots/tc10_empty_cart.png")
    assert home_page.is_cart_empty(),\
        "Cart is not empty after reset app state"
    print("Cart is empty")
