from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class EmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def open_employee_module(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Employee')]/ancestor::div[contains(@class, 'MuiBox-root')]"))).click()

    def click_create_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Create']]"))).click()

    def switch_to_contract_address_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Contact & Address']]"))).click()

    def select_country(self, country_name):
        Select(self.driver.find_element(By.XPATH, "//label[text()='Country']/following-sibling::div//input")).select_by_visible_text(country_name)

    def get_provinces(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "province")))
        options = self.driver.find_elements(By.XPATH, "//label[text()='Province']/following-sibling::div//input")
        return [opt.text.strip() for opt in options if opt.text.strip()]

    def select_province(self, province_name):
        Select(self.driver.find_element(By.XPATH, "//label[text()='Province']/following-sibling::div//input")).select_by_visible_text(province_name)

    def get_districts(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "district")))
        options = self.driver.find_elements(By.XPATH, '//input[@id="r4ai-label-District"]')
        return [opt.text.strip() for opt in options if opt.text.strip()]

    def select_district(self, district_name):
        Select(self.driver.find_element(By.XPATH, '//input[@id="r4ai-label-District"]')).select_by_visible_text(district_name)

    def get_wards(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "ward")))
        options = self.driver.find_elements(By.XPATH, '//input[@id="r4ci-label-Ward"]')
        return [opt.text.strip() for opt in options if opt.text.strip()]
