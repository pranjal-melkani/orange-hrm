from pages.loginpage import Loginpage
from pages.dashboardpage import Dashboardpage



class Testlogin:
    def test_valid_login(self, driver):
        username = "Admin"
        password = "admin123"

        lp = Loginpage(driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_on_login()
        is_logged_in = lp.is_logged_in()

        dp = Dashboardpage(driver)
        dp.logout()
        assert is_logged_in
        
    def test_invalid_credentials(self, driver):
        username = "asd"
        password = "asdsad"

        lp = Loginpage(driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_on_login()
        error_visible = lp.invalid_credentials_error_visible()
        assert error_visible