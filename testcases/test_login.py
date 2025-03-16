from pages.loginpage import Loginpage
from selenium.webdriver.common.by import By
import time
from base.basedriver import Basedriver


class Testlogin:
    def test_valid_login(self, driver):
        username = "Admin"
        password = "admin123"

        lp = Loginpage(driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_on_login()
        assert lp.is_logged_in()
        
