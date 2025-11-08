import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def accept_cookies(self):
        accept_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@class='cky-btn cky-btn-accept' and @aria-label='Accept All']")))
        accept_button.click()
       
    #Method to Sign in to the Platform with PIN.
    def login_with_pin(self, pin):
        pin_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='pin']")))
        pin_input.send_keys(pin)
        sign_in_button = self.wait.until(EC.element_to_be_clickable((By.ID, "sign-in-button")))
        sign_in_button.click()

    def click_brand_button(self):
        brand_button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "brd-01fvc8gs4sa9kjs8wxs6gnsn76")))
        brand_button.click()
