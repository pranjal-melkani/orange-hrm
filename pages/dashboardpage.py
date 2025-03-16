from base.basedriver import Basedriver

class Dashboardpage(Basedriver):
    USER_DROPDOWN = "//*[@class='oxd-userdropdown']"
    LOGOUT_BTN = "//*[@class='oxd-userdropdown-link' and text()='Logout']"

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click_on_element(self.USER_DROPDOWN)
        self.click_on_element(self.LOGOUT_BTN)
    