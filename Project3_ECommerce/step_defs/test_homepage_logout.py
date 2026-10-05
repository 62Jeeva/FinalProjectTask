import random

from pytest_bdd import given,when,then,scenarios

from pages.basepage import Basepage
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utils.excel_utility import read_login_data

scenarios("../features/Homepage_functioanlity.feature")

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

@then("user clicks on menu icon on the top left corner")
def user_clicks_menu_icon(driver):
    home_page = HomePage(driver)
    home_page.click(home_page.MENU_ICON)

@then("user clicks logout button")
def user_clicks_logout_button(driver):
    home_page = HomePage(driver)
    home_page.logout()
    assert driver.current_url == SAUCEDEMO_URL

@then("verify the cart icon is displayed")
def user_verify_cart_icon(driver):
    home_page = HomePage(driver)
    base_page  = Basepage(driver)
    assert home_page.is_cart_icon_displayed()
    base_page.take_screenshot("tc4_cart_icon_visibility")

@then("user able to select 4 products randomly and fetch their names and prices")
def random_product_selection(driver):
    home_page = HomePage(driver)
    product_names = home_page.get_product_names()
    product_prices = home_page.get_product_prices()
    print("Product Names:",product_names)
    print("Product Prices:",product_prices)
    products = list(zip(product_names, product_prices))
    selected_products = random.sample(products, 4)
    print("\nSelected 4 products:")
    for product in selected_products:
        name = product[0]
        price = product[1]
        print("\t", name, "\t", price)
    assert len(selected_products) == 4

@then("user able to select 4 products randomly and add them to cart")
def random_product_selection(driver):
    home_page = HomePage(driver)
    selected_products = home_page.add_random_products_to_cart()
    print("\nSelected products:")
    for product in selected_products:
        print(product)

@then("verify cart item count is 4")
def verify_cart_item_count(driver):
    home_page = HomePage(driver)
    cart_count = home_page.get_cart_count()
    assert cart_count == "4"
    print("Cart count:",cart_count)

@then("verify selected products are listed in the cart")
def verify_selected_products_in_cart(driver):
    home_page = HomePage(driver)
    home_page.click(home_page.CART_ICON)
    cart_products = home_page.get_cart_product_names()
    print("\nProducts in cart:")
    for product in cart_products:
        print(product)
    assert len(cart_products) == 4