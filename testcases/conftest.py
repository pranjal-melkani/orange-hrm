import pytest
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def driver():
    browser = webdriver.Edge()
    browser.maximize_window()
    browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield browser
    browser.quit()
