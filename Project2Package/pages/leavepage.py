from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.basepage import Basepage
from selenium.webdriver.support import expected_conditions as EC

class LeavePage(Basepage):

    LEAVE =(By.XPATH,"//span[text()='Leave']")
    ASSIGN_LEAVE = (By.XPATH,"//a[text()='Assign Leave']")
    EMPLOYEE_NAME = (By.XPATH,"//input[@placeholder='Type for hints...']")
    EMPLOYEE_NAME_SUGGESTION = (By.CSS_SELECTOR,"div[role='listbox'] div[role='option']")
    LEAVE_DROPDOWN = (By.XPATH,"//label[text()='Leave Type']/ancestor::div[contains(@class,'oxd-input-group')]//div[@class='oxd-select-wrapper']")
    LEAVE_TYPE = (By.XPATH,"//div[@role='listbox']//span[text()='CAN - Personal']")
    FROM_DATE =(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/input")
    TO_DATE=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input")
    COMMENTS=(By.XPATH,"//textarea[@class ='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
    ASSIGN=(By.XPATH,"//button[@type='submit']")
    MY_LEAVE=(By.XPATH,"//a[text()='My Leave']")
    OK_BUTTON = (By.XPATH,"//*[@id='app']/div[3]/div/div/div/div[3]/button[2]")

    def click_assign_leave(self):
        self.click(self.ASSIGN_LEAVE)

    def enter_employee_name(self,employee_name):
        self.enter_text(self.EMPLOYEE_NAME,employee_name)

    def select_employee_name(self,employee_name):
        suggestion_locator = (
            By.CSS_SELECTOR,
            "div[role='listbox'] div[role='option']"
        )
        self.wait.until(
            lambda driver: any(
                option.text.strip() != "Searching...."
                for option in driver.find_elements(*suggestion_locator)
            )
        )
        suggestions = self.driver.find_elements(*suggestion_locator)
        for suggestion in suggestions:
            if employee_name in suggestion.text:
                suggestion.click()
                return
        raise Exception(
            f"Employee '{employee_name}' was not found in suggestions"
        )

    def click_leave_type(self):
        self.click(self.LEAVE_DROPDOWN)
        self.click(self.LEAVE_TYPE)

    def enter_from_date(self,date):
        element_selection = self.wait.until(EC.element_to_be_clickable(self.FROM_DATE))
        element_selection.click()
        element_selection.clear()
        element_selection.send_keys(date)
        element_selection.send_keys(Keys.ARROW_DOWN)
        element_selection.send_keys(Keys.ENTER)

    def enter_to_date(self,date):
        element_selection = self.wait.until(EC.element_to_be_clickable(self.TO_DATE))
        element_selection.click()
        element_selection.send_keys(Keys.CONTROL,"a")
        element_selection.send_keys(date)
        element_selection.send_keys(Keys.ENTER)

    def enter_comments(self,comments):
        self.enter_text(self.COMMENTS,comments)

    def click_assignment_leave(self):
       try:
            self.click(self.ASSIGN)
       except Exception:
            self.click(self.OK_BUTTON)

    def click_my_leave(self):
        self.click(self.MY_LEAVE)

