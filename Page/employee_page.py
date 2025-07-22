import time

import self
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class EmployeePage:
    def __init__(self, driver):
        self.driver = driver

    def open_employee_module(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Employee')]/ancestor::div[contains(@class, 'MuiBox-root')]"))).click()

    def click_create_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div[3]/div/div/div/div[2]/div[1]/div/button[5]'))).click()

    def switch_to_contract_address_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='Contact & Address']]"))).click()

    def select_country(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div'))).click()

    def click_country(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.MuiAutocomplete-listbox"))
        )
        indonesia_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='INDONESIA']"))
        )
        indonesia_option.click()

    def select_province(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div'))).click()

    def click_province(self):
        try:
            # Wait for the autocomplete list to be visible
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.MuiAutocomplete-listbox"))
            )

            retries = 3
            for attempt in range(retries):
                try:

                    first_province_option = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//ul[@role='listbox']//p[contains(text(), 'Provinsi Aceh')]"))
                    )

                    # Scroll to the element to ensure it's in view
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", first_province_option)
                    time.sleep(0.5)  # Small delay to ensure scroll completes

                    # Attempt to click
                    first_province_option.click()
                    return  # Exit if click is successful

                except (TimeoutException, StaleElementReferenceException) as e:
                    print(f"Attempt {attempt + 1} failed: {str(e)}")
                    if attempt == retries - 1:
                        raise TimeoutException("Failed to click 'Provinsi Aceh' after retries")
                    time.sleep(1)  # Wait before retrying

        except TimeoutException as e:
            print(f"Error: Autocomplete list not found or province not clickable: {str(e)}")
            raise

    def select_district(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[3]/div'))).click()

    def click_regency(self):
        try:
            # Wait for the autocomplete list to be visible
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.MuiAutocomplete-listbox"))
            )

            # Retry mechanism to handle dynamic DOM or stale elements
            retries = 3
            for attempt in range(retries):
                try:
                    # Use a flexible XPath to locate the regency
                    regency_option = WebDriverWait(self.driver, 15).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//ul[@role='listbox']//p[contains(text(), 'Kabupaten Aceh Selatan')]"))
                    )

                    # Scroll to the element to ensure it's in view
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", regency_option)
                    time.sleep(0.5)  # Small delay to ensure scroll completes

                    # Attempt to click
                    regency_option.click()
                    print("Clicked 'Kabupaten Aceh Selatan'")
                    return  # Exit if click is successful

                except (TimeoutException, StaleElementReferenceException) as e:
                    print(f"Attempt {attempt + 1} failed to click 'Kabupaten Aceh Selatan': {str(e)}")
                    if attempt == retries - 1:
                        self.driver.save_screenshot("regency_click_error.png")
                        raise TimeoutException("Failed to click 'Kabupaten Aceh Selatan' after retries")
                    time.sleep(1)  # Wait before retrying

        except TimeoutException as e:
            print(f"Error: Autocomplete list not found or regency not clickable: {str(e)}")
            self.driver.save_screenshot("regency_error.png")
            # Debug: Check if the element exists
            elements = self.driver.find_elements(By.XPATH,
                                                 "//ul[@role='listbox']//p[contains(text(), 'Kabupaten Aceh Selatan')]")
            print(f"Found {len(elements)} elements matching 'Kabupaten Aceh Selatan'")
            if elements:
                print(elements[0].get_attribute("outerHTML"))
            raise
    def select_ward(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div[3]/div/div/div[4]/div'))).click()

    def click_ward(self):
        try:
            # Wait for the autocomplete list to be visible
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.MuiAutocomplete-listbox"))
            )

            # Retry mechanism to handle dynamic DOM or stale elements
            retries = 3
            for attempt in range(retries):
                try:
                    # Use a flexible XPath to locate the district
                    district_option = WebDriverWait(self.driver, 15).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//ul[@role='listbox']//p[contains(text(), 'Kecamatan Bakongan')]"))
                    )

                    # Scroll to the element to ensure it's in view
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", district_option)
                    time.sleep(0.5)  # Small delay to ensure scroll completes

                    # Attempt to click
                    district_option.click()
                    print("Clicked 'Kecamatan Bakongan'")
                    return  # Exit if click is successful

                except (TimeoutException, StaleElementReferenceException) as e:
                    print(f"Attempt {attempt + 1} failed to click 'Kecamatan Bakongan': {str(e)}")
                    if attempt == retries - 1:
                        self.driver.save_screenshot("district_click_error.png")
                        raise TimeoutException("Failed to click 'Kecamatan Bakongan' after retries")
                    time.sleep(1)  # Wait before retrying

        except TimeoutException as e:
            print(f"Error: Autocomplete list not found or district not clickable: {str(e)}")
            self.driver.save_screenshot("district_error.png")
            # Debug: Check if the element exists
            elements = self.driver.find_elements(By.XPATH,
                                                 "//ul[@role='listbox']//p[contains(text(), 'Kecamatan Bakongan')]")
            print(f"Found {len(elements)} elements matching 'Kecamatan Bakongan'")
            if elements:
                print(elements[0].get_attribute("outerHTML"))
            # Debug: Log available lists
            lists = self.driver.find_elements(By.CSS_SELECTOR, "ul.MuiAutocomplete-listbox")
            print(f"Found {len(lists)} autocomplete lists")
            if lists:
                print(lists[0].get_attribute("outerHTML"))
            raise
