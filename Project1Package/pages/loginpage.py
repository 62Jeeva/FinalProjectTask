from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Project1Package.pages.basepage import Basepage


class LoginPage(Basepage):

    MAIN_LOGIN =(By.XPATH,"//button[@id='login-btn']")
    SIGN_UP = (By.XPATH,"(//button[text()='Sign up'][1])")
    EMAIL=(By.ID,'email')
    PASSWORD=(By.ID,'password')
    LOGIN_BUTTON=(By.XPATH,"//a[@id='login-btn']")
    INVALID_EMAIL_PASSWORD = (By.XPATH,"(//div[contains(text(),'Incorrect Email or Password')])[1]")
    INVALID_EMAIL_MESSAGE = (By.XPATH,"//div[contains(@class,'invalid-feedback') and contains(text(),'doesnt look like an email address')]")

    def launch_url(self):
        self.open_url("https://www.guvi.in")


    def login(self,email,password):
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BUTTON)

    def validate_username(self, username):
        self.enter_text(self.EMAIL, username)
        return self.get_attribute(self.EMAIL, "value")

    def validate_password(self,password):
        self.enter_text(self.PASSWORD,password)
        return self.get_attribute(self.PASSWORD,"value")

    def main_login_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.MAIN_LOGIN)).is_displayed()

    def click_login_btn(self):
        self.click_element(self.MAIN_LOGIN)

    def sign_up_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.SIGN_UP)).is_displayed()

    def click_sign_up(self):
        self.click_element(self.SIGN_UP)

    def login_button_enabled(self):
        return self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).is_enabled()

    def invalid_email_password(self):
        return self.get_text(self.INVALID_EMAIL_PASSWORD)

    def invalid_email_message(self):
        return self.get_text(self.INVALID_EMAIL_MESSAGE)