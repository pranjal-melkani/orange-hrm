from base.basedriver import Basedriver


class Loginpage(Basedriver):
    USERNAME_FIELD = "//*[@placeholder='Username']"
    PASSWORD_FIELD = "//*[@placeholder='Password']"
    LOGIN_BTN = "//*[contains(@class, 'orangehrm-login-button')]"
    FORGOT_PASSWORD_LINK = "//*[contains(@class, 'orangehrm-login-forgot-header')]"

    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_on_login(self):
        self.click_on_element(self.LOGIN_BTN)
    
    def click_on_forgot_password(self):
        self.click_on_element(self.FOR)

    def is_logged_in(self):
        try:
            self.wait_until_element_is_visible("//header//*[text()='Dashboard']")
            return True
        except Exception:
            return False