import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TitlePage:
    def __init__(self, driver):
        self.driver = driver

    #Method to navigate to the 'Test Automation Project':
    def scroll_to_test_project(self):
        #Navigate to the "All Titles" screen.
        target_div = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h5[text()='Test automation project']/ancestor::div[contains(@class, 'wds-flex')]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target_div)
        time.sleep(5)

    #Method to locate and click on the Test automation project.
    def open_test_project(self):
        wait = WebDriverWait(self.driver, 10)
        project = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//h5[contains(text(),'Test automation project')]")))
        project.click()
