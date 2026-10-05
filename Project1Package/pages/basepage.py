import os

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

    def click_element(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self,locator):
       return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def get_title(self):
        return  self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_attribute(self, locator, attribute):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute)

    def take_screenshot(self,file_name):
        os.makedirs("screenshots", exist_ok=True)

        file_path = f"screenshots/{file_name}.png"

        self.driver.save_screenshot(file_path)

        print(f"Screenshot saved: {file_path}")


    def close_browser(self):
        self.driver.quit()
