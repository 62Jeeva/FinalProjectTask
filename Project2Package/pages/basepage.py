import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver,timeout=20,poll_frequency=2)


    def open_url(self,url):
        self.driver.get(url)

    def enter_text(self,locator,value):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self,locator):
       return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def take_screenshot(self,file_name):
        self.driver.save_screenshot(f"screenshots/{file_name}.png")

    def close_browser(self):
        self.driver.quit()
