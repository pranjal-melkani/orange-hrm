from base.basedriver import Basedriver
from selenium.webdriver.common.keys import Keys
import time

class Dashboardpage(Basedriver):
    USER_DROPDOWN = "//*[@class='oxd-userdropdown']"
    LOGOUT_BTN = "//*[@class='oxd-userdropdown-link' and text()='Logout']"
    ADMIN_LINK = "//*[text()='Admin']"
    ADD_USER_BTN = "//*[@class='orangehrm-header-container']//button"
    USER_ROLE_DROPDOWN = "//*[text()='User Role']//parent::div//parent::div//*[contains(@class,'oxd-select-text ')]//*[@class='oxd-select-text--after']"
    USER_ROLE_FIELD = "//*[text()='User Role']//parent::div//parent::div//*[contains(@class,'oxd-select-text ')]//*[@class='oxd-select-text-input']"
    EMP_NAME_FIELD = "//*[text()='Employee Name']//parent::div//parent::div//input"
    STATUS_DROPDOWN = "//*[text()='Status']//parent::div//parent::div//*[contains(@class,'oxd-select-text ')]//*[@class='oxd-select-text--after']"
    STATUS_FIELD = "//*[text()='Status']//parent::div//parent::div//*[contains(@class,'oxd-select-text ')]//*[@class='oxd-select-text-input']"
    USERNAME_FIELD = "//*[text()='Username']//parent::div//parent::div//input"
    PASSWORD_FIELD = "//*[text()='Password']//parent::div//parent::div//input"
    CONFIRM_PASSWORD_FIELD = "//*[text()='Confirm Password']//parent::div//parent::div//input"
    SAVE_BTN = "//*[contains(@class, 'oxd-button--secondary')]"
    USER_LIST_TABLE = "//*[text()='{user_name}']//parent::div//parent::div[contains(@class,'oxd-table-row ')]//*[contains(@class,'oxd-table-cell ') and @class!='oxd-table-cell-actions'][{column_no}]//div"

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click_on_element(self.USER_DROPDOWN)
        self.click_on_element(self.LOGOUT_BTN)
    
    def go_to_admin_section(self):
        self.click_on_element(self.ADMIN_LINK)
    
    def click_on_add_user(self):
        self.click_on_element(self.ADD_USER_BTN)

    def select_user_role(self, user_role):
        self.click_on_element(self.USER_ROLE_DROPDOWN)
        current_value = self.wait_until_element_is_visible(self.USER_ROLE_FIELD).text
        while(current_value.lower() != user_role.lower()):
            self.send_keys(self.USER_ROLE_FIELD, Keys.DOWN)
            current_value = self.wait_until_element_is_visible(self.USER_ROLE_FIELD).text
        self.send_keys(self.USER_ROLE_FIELD, Keys.ENTER)

    def enter_emp_name(self, emp_name):
        self.send_keys(self.EMP_NAME_FIELD, emp_name)
        time.sleep(2)
        self.send_keys(self.EMP_NAME_FIELD, Keys.DOWN)
        self.send_keys(self.EMP_NAME_FIELD, Keys.ENTER)

    def select_status(self, status):
        self.click_on_element(self.STATUS_DROPDOWN)
        current_value = self.wait_until_element_is_visible(self.STATUS_FIELD).text
        while(current_value.lower() != status.lower()):
            self.send_keys(self.STATUS_FIELD, Keys.DOWN)
            current_value = self.wait_until_element_is_visible(self.STATUS_FIELD).text
        self.send_keys(self.STATUS_FIELD, Keys.ENTER)

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)
        time.sleep(2)
        self.send_keys(self.USERNAME_FIELD, Keys.ENTER)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)
        self.send_keys(self.CONFIRM_PASSWORD_FIELD, password)

    def click_on_save(self):
        self.click_on_element(self.SAVE_BTN)

    def check_if_user_exists(self, username, user_role, emp_name, status):
        try:
            self.wait_until_element_is_visible(self.USER_LIST_TABLE.format(user_name=username, column_no=2))
            _username = self.wait_until_element_is_visible(self.USER_LIST_TABLE.format(user_name=username, column_no=2)).text
            if _username.lower() == username.lower():
                print("username matched")
            else:
                print(f"username not matched. Found {_username} instead of {username}")
                raise Exception
            
            _user_role = self.wait_until_element_is_visible(self.USER_LIST_TABLE.format(user_name=username, column_no=3)).text
            if _user_role.lower() == user_role.lower():
                print("user role matched")
            else:
                print(f"user role not matched. Found {_user_role} instead of {user_role}")
                raise Exception
            
            _emp_name = self.wait_until_element_is_visible(self.USER_LIST_TABLE.format(user_name=username, column_no=4)).text
            if emp_name.lower() in _emp_name.lower():
                print("emp_name matched")
            else:
                print(f"emp_name not matched. Found {_emp_name} instead of {emp_name}")
                raise Exception
            
            _status = self.wait_until_element_is_visible(self.USER_LIST_TABLE.format(user_name=username, column_no=5)).text
            if _status.lower() == status.lower():
                print("status matched")
            else:
                print(f"status not matched. Found {_status} instead of {status}")
                raise Exception
            
            return True
        except Exception:
            return False

