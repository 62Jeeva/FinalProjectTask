from selenium.webdriver.common.by import By
from pages.basepage import Basepage
from selenium.webdriver.support import expected_conditions as EC

class ClaimPage(Basepage):

    MENU_CLAIM =(By.XPATH,"//span[text()='Claim']")
    SUBMIT_CLAIM =(By.XPATH,"//a[text()='Submit Claim']")
    EVENT_DROPDOWN = (By.XPATH,"(//div[text()='-- Select --'])[1]")
    EVENT_SELECTION = (By.CSS_SELECTOR,"div[role='listbox'] div[role='option']")
    CURRENCY_DROPDOWN =(By.XPATH,"(//div[contains(@class,'oxd-select-text-input')])[2]")
    CURRENCY_SELECTION = (By.CSS_SELECTOR,"div[role='listbox'] div[role='option']")
    REMARKS =(By.XPATH,"//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
    CREATE_BUTTON =(By.XPATH,"//button[@type='submit']")
    MY_CLAIMS=(By.XPATH,"//a[text()='My Claims']")
    MY_CLAIMS_VERIFY =(By.XPATH,"//h5[text()='My Claims']")
    RECORD_VERIFY=(By.XPATH,"//div[@class='oxd-table-card']")

    def click_claim(self):
        self.click(self.MENU_CLAIM)

    def click_submit_claim(self):
        self.click(self.SUBMIT_CLAIM)

    def click_event_dropdown(self):
        self.click(self.EVENT_DROPDOWN)
        options = self.driver.find_elements(By.CSS_SELECTOR,"div[role='listbox'] div[role='option']")
        print("Event dropdown options")
        for option in options:
            print(option.text)
            if option.text.strip() == "Accommodation":
                option.click()
                return

    def click_currency_dropdown(self):
        currency_fields = self.driver.find_elements(By.CSS_SELECTOR,"div.oxd-select-text-input")
        print("No of fields:",len(currency_fields))
        for index,field in enumerate(currency_fields):
            print(index,":",field.text)
        self.click(self.CURRENCY_DROPDOWN)
        currency_dropdown = self.driver.find_element(By.CSS_SELECTOR,"div[role='listbox'].oxd-select-dropdown")
        options = currency_dropdown.find_elements(By.CSS_SELECTOR,"div[role='option']")
        print("Currency dropdown options")
        for option in options:
            print(option.text)

            if option.text.strip() == "Indian Rupee":
                option.click()
                return

    def enter_remarks(self,remarks):
        self.enter_text(self.REMARKS,remarks)

    def click_create(self):
        self.click(self.CREATE_BUTTON)

    def click_my_claims(self):
        self.click(self.MY_CLAIMS)
        self.wait.until(lambda driver:"/claim/viewClaim" in driver.current_url)
        self.wait.until(EC.visibility_of_element_located(self.MY_CLAIMS_VERIFY)
        )

    def scroll_to_record(self):
        element = self.wait.until(
        EC.visibility_of_element_located(self.RECORD_VERIFY)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )