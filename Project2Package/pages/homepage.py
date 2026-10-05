from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from pages.basepage import Basepage

class HomePage(Basepage):

    HOMEPAGE_DASHBOARD = (By.XPATH,"//h6[text()='Dashboard']")
    PROFILE = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    LOGOUT = (By.XPATH,"//a[text() ='Logout']")
    ADMIN = (By.XPATH, "//span[text()='Admin']")
    PIM = (By.XPATH, "//span[text()='PIM']")
    LEAVE = (By.XPATH, "//span[text()='Leave']")
    TIME = (By.XPATH, "//span[text()='Time']")
    RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    MY_INFO = (By.XPATH, "//span[text()='My Info']")
    PERFORMANCE = (By.XPATH, "//span[text()='Performance']")
    DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    CLAIM = (By.XPATH, "//span[text()='Claim']")

    def login(self):
        try:
          return self.wait.until(EC.visibility_of_element_located(self.HOMEPAGE_DASHBOARD)).is_displayed()
        except TimeoutException:
            return False

    def is_homepage_displayed(self):
        return self.is_displayed(self.HOMEPAGE_DASHBOARD)

    def click_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN)).click()

    def click_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.PIM)).click()

    def click_leave(self):
        self.wait.until(EC.element_to_be_clickable(self.LEAVE)).click()

    def click_time(self):
        self.wait.until(EC.element_to_be_clickable(self.TIME)).click()

    def click_recruitment(self):
        self.wait.until(EC.element_to_be_clickable(self.RECRUITMENT)).click()

    def click_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO)).click()

    def click_performance(self):
        self.wait.until(EC.element_to_be_clickable(self.PERFORMANCE)).click()

    def click_dashboard(self):
        self.wait.until(EC.element_to_be_clickable(self.DASHBOARD)).click()

    def click_claim(self):
        self.wait.until(EC.element_to_be_clickable(self.CLAIM)).click()

    def verify_menu_items(self):
        menu_items = [self.ADMIN,
                      self.PIM,
                      self.LEAVE,
                      self.TIME,
                      self.RECRUITMENT,
                      self.MY_INFO,
                      self.PERFORMANCE,
                      self.DASHBOARD
                      ]
        for item in menu_items:
            self.wait.until(EC.element_to_be_clickable(item))


    def click_each_menu_item(self):
        self.click_admin()
        self.click_pim()
        self.click_leave()
        self.click_time()
        self.click_recruitment()
        self.click_my_info()
        self.click_performance()
        self.click_dashboard()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()
        self.wait.until(EC.url_contains("auth/login"))


    def close_browseroperation(self):
        self.close_browser()
