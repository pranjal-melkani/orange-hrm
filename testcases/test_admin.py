from pages.loginpage import Loginpage
from pages.dashboardpage import Dashboardpage
from faker import Faker

class Test_UserManagement:
    def test_add_user(self, driver):
        username = "Admin"
        password = "admin123"
        user_role = 'admin'
        emp_name = "Peter"
        status = "enabled"
        
        lp = Loginpage(driver)
        lp.enter_username(username)
        lp.enter_password(password)
        lp.click_on_login()

        username = Faker().user_name()
        password = "Password@123"

        dp = Dashboardpage(driver)
        dp.go_to_admin_section()
        dp.click_on_add_user()
        dp.select_user_role(user_role)
        dp.enter_emp_name(emp_name)
        dp.select_status(status)
        print(username)
        dp.enter_username(username)
        dp.enter_password(password)
        dp.click_on_save()
        user_exists = dp.check_if_user_exists(username,user_role,emp_name,status)
        assert user_exists
