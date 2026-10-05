from selenium.webdriver.common.by import By
from pages.basepage import Basepage
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage(Basepage):
    MY_INFO = (By.XPATH, "//span[text()='My Info']")
    CONTACT_DETAILS =(By.XPATH,"//a[text()='Contact Details']")
    EMERGENCY = (By.XPATH,"//a[contains(text(),'Emergency')]")
    DEPENDENTS = (By.XPATH,"//a[text() = 'Dependents']")
    IMMIGRATION = (By.XPATH,"//a[text() = 'Immigration']")
    JOB = (By.XPATH,"//a[text()='Job']")
    SALARY = (By.XPATH,"//a[text()='Salary']")
    REPORT_TO =(By.XPATH,"//a[text()='Report-to']")
    QUALIFICATION =(By.XPATH,"//a[text() = 'Qualifications']")
    MEMBERSHIPS =(By.XPATH,"//a[text()='Memberships']")

    def click_contact_details(self):
        self.click(self.CONTACT_DETAILS)

    def click_emergency(self):
        self.click(self.EMERGENCY)

    def click_dependents(self):
        self.click(self.DEPENDENTS)

    def click_immigration(self):
        self.click(self.IMMIGRATION)

    def click_job(self):
        self.click(self.JOB)

    def click_salary(self):
        self.click(self.SALARY)

    def click_report_to(self):
        self.click(self.REPORT_TO)

    def click_qualifications(self):
        self.click(self.QUALIFICATION)

    def click_memberships(self):
        self.click(self.MEMBERSHIPS)

    def verify_sub_menu_items(self):
        menu_items = [
            self.CONTACT_DETAILS,
            self.EMERGENCY,
            self.DEPENDENTS,
            self.IMMIGRATION,
            self.JOB,
            self.SALARY,
            self.REPORT_TO,
            self.QUALIFICATION,
            self.MEMBERSHIPS
        ]
        for item in menu_items:
            self.wait.until(EC.element_to_be_clickable(item))

    def is_contact_details_page(self):
        return "contactDetails" in self.get_current_url()

    def is_emergency_contacts_page(self):
        return "viewEmergencyContacts" in self.get_current_url()

    def is_dependents_page(self):
        return "viewDependents" in self.get_current_url()

    def is_immigration_page(self):
        return "viewImmigration" in self.get_current_url()

    def is_job_page(self):
        return "viewJobDetails" in self.get_current_url()

    def is_salary_page(self):
        return "viewSalaryList" in self.get_current_url()

    def is_report_to_page(self):
        return "viewReportToDetails" in self.get_current_url()

    def is_qualifications_page(self):
        return "viewQualifications" in self.get_current_url()

    def is_memberships_page(self):
        return "viewMemberships" in self.get_current_url()