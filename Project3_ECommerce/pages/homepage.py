import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.basepage import Basepage


class HomePage(Basepage):
    MENU_ICON = (By.XPATH, "//button[text()='Open Menu']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")
    CART_ICON = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='inventory_item_name']")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    PRODUCTS = (By.XPATH, "//div[@class='inventory_item']")
    ADD_TO_CART = (By.XPATH, "//button[text() ='Add to cart']")
    CART_ITEM_COUNT_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_PRODUCT_NAME = (By.XPATH, "//div[@class='cart_item']//div[@class='inventory_item_name']")
    CART_PRODUCT_PRICE = (By.XPATH, "//div[@class='cart_item']//div[@class='inventory_item_price']")
    SORT_DROPDOWN = (By.XPATH, "//select[@class='product_sort_container']")
    RESET_APP_STATE = (By.XPATH, "//a[@id='reset_sidebar_link']")


    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click(self.MENU_ICON)
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        print("After Logout URL:", self.get_current_url())

    def is_cart_icon_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_ICON)).is_displayed()

    def get_product_names(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        product_names = []
        for product in products:
            product_name = product.text.split("\n")[0]
            product_names.append(product_name)
        return product_names

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICE)
        return [price.text for price in prices]

    def add_random_products_to_cart(self):
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCTS))
        products = self.driver.find_elements(*self.PRODUCTS)
        # selecting the 4 random product indexes
        selected_indexes = random.sample(range(len(products)), 4)
        selected_names = []
        selected_prices = []
        for index in selected_indexes:
            product = products[index]
            product_details = product.text.split("\n")
            product_name = product_details[0]
            product_price = product_details[2]
            selected_names.append(product_name)
            selected_prices.append(product_price)

        #clicking each product by finding the product element again
        for position, product_name in enumerate(selected_names, start=1):

            products = self.driver.find_elements(*self.PRODUCTS)
            product = None
            for item in products:
                current_name = item.text.split("\n")[0]
                if current_name == product_name:
                    product = item
                    break

            if product is None:
                raise Exception(f"Product not found: {product_name}")
            add_button = product.find_element(
                By.XPATH,
                ".//button[contains(@class,'btn_inventory')]"
            )
            add_button.click()
            # waiting time till the cart reaches the 4 products
            self.wait.until(lambda driver:(driver.find_elements(*self.CART_ITEM_COUNT_BADGE)
                                           and driver.find_element(*self.CART_ITEM_COUNT_BADGE).text == str(position)))
        self.driver.selected_names = selected_names
        self.driver.selected_prices = selected_prices
        return selected_names, selected_prices


    def get_cart_product_names(self):
        cart_products = self.driver.find_elements(*self.CART_PRODUCT_NAME)
        print("Number of cart products:", len(cart_products))
        cart_names = [product.text for product in cart_products]
        print("Cart product names:", cart_names)
        return cart_names


    def get_cart_product_prices(self):
        cart_prices = self.driver.find_elements(*self.CART_PRODUCT_PRICE)
        print("Number of cart prices:", len(cart_prices))
        prices = [price.text for price in cart_prices]
        print("Cart prices:", prices)
        return prices


    def get_cart_count(self):
        cart_badge = self.wait.until(EC.visibility_of_element_located(self.CART_ITEM_COUNT_BADGE))
        return cart_badge.text


    def click_cart_icon(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.CART_ICON))
        cart.click()
        self.wait.until(EC.url_contains("/cart.html"))


    def select_sort_option(self, option):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_visible_text(option)


    def reset_app_state(self):
        self.wait.until(EC.element_to_be_clickable(self.RESET_APP_STATE)).click()


    def is_cart_empty(self):
        cart_badge = self.driver.find_elements(*self.CART_ITEM_COUNT_BADGE)
        return len(cart_badge) == 0
