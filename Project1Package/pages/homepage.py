from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from Project1Package.pages.basepage import Basepage


class HomePage(Basepage):

    PROFILE_ICON = (By.XPATH, "(//img[@alt='Profile'])[1]")
    LOGOUT_BUTTON = (By.XPATH, "(//p[text() ='Sign Out']/ancestor::div[@id='signout'])[1]")
    LIVE_CLASSES = (By.XPATH,"(//p[text()='LIVE Classes'])[1]")
    COURSES = (By.XPATH,"(//p[text()='Courses'])[1]")
    PRACTICE =(By.XPATH,"(//p[text()='Practice'])[1]")
    DOBBY_ASSISTANT = (By.XPATH,"//span[@aria-label='Chat Widget']")


    def verify_login(self):
        return self.wait.until(EC.visibility_of_element_located(self.PROFILE_ICON)).is_displayed()

    def perform_operation(self):
        print("Page Title: ", self.get_title())
        print("Current URL: ", self.get_current_url())

    def validate_menu(self):
        return (self.is_displayed(self.LIVE_CLASSES) and self.is_displayed(self.COURSES) and self.is_displayed(self.PRACTICE))

    def dobby_assistant(self):
        return self.is_displayed(self.DOBBY_ASSISTANT)

    def logout(self):
        self.click_element(self.PROFILE_ICON)
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        print("After Logout URL:", self.get_current_url())

    def verify_logout(self):
        return self.is_displayed(self.LOGOUT_BUTTON)

    def close_browseroperation(self):
        self.close_browser()
