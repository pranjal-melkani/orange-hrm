from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basedriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_visible(self, xpath):
        wait = WebDriverWait(self.driver, timeout=10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element
    
    def click_on_element(self, xpath):
        element = self.wait_until_element_is_visible(xpath)
        element.click()

    def send_keys(self, xpath, input_text):
        element = self.wait_until_element_is_visible(xpath)
        element.send_keys(input_text)

    def get_current_title(self):
        return self.driver.title
    
    def go_back(self):
        self.driver.back()