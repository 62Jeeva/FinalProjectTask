from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.basepage import Basepage


class CheckoutPage(Basepage):
    CHECKOUT_BUTTON = (By.XPATH,"//button[@id='checkout']")
    FIRST_NAME = (By.XPATH,"//input[@id='first-name']")
    LAST_NAME = (By.XPATH,"//input[@id='last-name']")
    POSTCODE = (By.XPATH,"//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH,"//input[@id='continue']")
    FINISH_BUTTON = (By.XPATH,"//button[@id='finish']")
    ORDER_CONFIRMATION_MSG = (By.XPATH,"//h2[@class='complete-header']")



    def __init__(self,driver):
        super().__init__(driver)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def enter_customer_information(self,firstname,lastname,postalcode):
        self.enter_text(self.FIRST_NAME,firstname)
        self.enter_text(self.LAST_NAME,lastname)
        self.enter_text(self.POSTCODE,postalcode)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_order_confirmation_message(self):
        try:
            return self.get_text(self.ORDER_CONFIRMATION_MSG)
        except TimeoutException:
            print("Order confirmation message not displayed")
            raise