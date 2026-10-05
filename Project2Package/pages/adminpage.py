import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from pages.basepage import Basepage

class AdminPage(Basepage):

    ADD = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
    ADMIN_DROPDOWN= (By.XPATH, "(//div[text()='-- Select --'])[1]")
    ADMIN_USER_ROLE =(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active']/div[@tabindex='0'])[1]")
    ADMIN_ROLE_OPTION =(By.XPATH,"//div[@role='option']//span[text() = 'Admin']")
    ADMIN_EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SUGGESTION = (By.XPATH,"//div[@class='oxd-autocomplete-text-input--after']")
    STATUS = (By.XPATH,"(//div[contains(@class,'oxd-select-text')])[4]")
    ENABLED_STATUS = (By.XPATH,"//div[@role='option']//span[text()='Enabled']")
    ADMIN_USERNAME =(By.XPATH,"(//input[@class ='oxd-input oxd-input--active'])[2]")
    ADMIN_PASSWORD=(By.XPATH,"(//input[@type='password'])[1]")
    ADMIN_CONFIRM_PASSWORD=(By.XPATH,"(// input[@type='password'])[2]")
    SAVE=(By.XPATH,"//button[@type='submit']")
    ADMIN =(By.XPATH,"// span[text() = 'Admin']")
    USER_MANAGEMENT =(By.XPATH,"// h6[text() = 'User Management']")
    SEARCH_USERNAME = (By.XPATH,"(//input[@class ='oxd-input oxd-input--active'])[2]")
    SEARCH=(By.XPATH,"// button[@ type='submit']")
    RECORD_VERIFY =(By.XPATH,"//div[@class='oxd-table-card']")



    def click_add(self):
        self.click(self.ADD)

    def click_user_role_dropdown(self):
        self.click(self.ADMIN_USER_ROLE)

    def enter_employee_name(self,employee_name):
        self.enter_text(self.ADMIN_EMPLOYEE_NAME,employee_name)

    def select_employee_name(self,employee_name):
        self.wait.until(lambda driver:driver.find_elements(By.XPATH,"//div[@role='listbox']")
                                   and driver.find_element(By.XPATH,"//div[@role='listbox']").text!="Searching....")
        print("Suggestion after search:",self.driver.find_element(By.XPATH,"//div[@role='listbox']").text)
        suggestion =  self.wait.until(EC.element_to_be_clickable((By.XPATH,f"//div[@role='listbox']//*[normalize-space(text())='{employee_name}']")))
        suggestion.click()

    def click_status_dropdown(self):
        self.click(self.STATUS)

    def select_enabled_status(self):
        self.click(self.STATUS)
        self.click(self.ENABLED_STATUS)

    def enter_username(self,username):
        element = self.wait.until(EC.visibility_of_element_located(self.ADMIN_USERNAME))
        element.clear()
        for char in username:
            element.send_keys(char)

    def enter_password(self,password):
        self.enter_text(self.ADMIN_PASSWORD,password)

    def enter_confirm_password(self,password):
        self.enter_text(self.ADMIN_CONFIRM_PASSWORD,password)

    def click_save(self):
        self.click(self.SAVE)

    def is_user_management_displayed(self):
        return self.is_displayed(self.USER_MANAGEMENT)

    def enter_search_username(self,username):
        self.enter_text(self.SEARCH_USERNAME,username)

    def click_search(self):
        self.click(self.SEARCH)

    def select_admin_role(self):
        self.click(self.ADMIN_ROLE_OPTION)

    def scroll_to_record(self):
        element = self.wait.until(
        EC.visibility_of_element_located(self.RECORD_VERIFY)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

