from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.basepage import Basepage

class LoginPage(Basepage):
    USERNAME = (By.ID,"user-name")
    PASSWORD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-button")
    ERROR_MESSAGE = (By.XPATH,"//h3[@data-test='error']")


    def enter_username(self,username):
        self.enter_text(self.USERNAME,username)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD,password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver,60).until(EC.url_contains("/inventory.html"))
            return True
        except TimeoutException:
            return False

    def is_error_displayed(self):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return True
        except TimeoutException:
            return False

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)



