from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import Basepage

class LoginPage(Basepage):

    USERNAME=(By.XPATH,"//input[@name='username']")
    PASSWORD=(By.XPATH,"//input[@name='password']")
    lOGIN_BUTTON=(By.XPATH,"//button[@type='submit']")
    VERIFY_ERROR=(By.XPATH,"//div[@role='alert']")
    VERIFY_DASHBOARD =(By.XPATH,"//h6[text()='Dashboard']")
    FORGOT_YOUR_PASSWORD = (By.XPATH,"//p[text()='Forgot your password? ']")
    RESET_PASSWORD =(By.XPATH,"//button[@type='submit']")


    def open_login_page(self):
        self.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self,username):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self,password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def is_username_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.USERNAME)).is_displayed()

    def is_password_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).is_displayed()

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.lOGIN_BUTTON)).click()

    def wait_for_dashboard(self):
        self.wait.until(EC.visibility_of_element_located(self.VERIFY_DASHBOARD))

    def invalid_error_message(self):
        self.wait.until(EC.visibility_of_element_located(self.VERIFY_ERROR))

    def click_forgot_password(self):
        self.click(self.FORGOT_YOUR_PASSWORD)

    def enter_reset_username(self,username):
        self.enter_text(self.USERNAME,username)

    def click_reset_password(self):
        self.click(self.RESET_PASSWORD)