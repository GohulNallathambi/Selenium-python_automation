import time

import pytest
from selenium.webdriver.common.by import By

from Pom.Base.Base_driver import BaseDriver
from Pom.Config.config import TestData


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.driver.get(TestData.BASE_URL)

    def test_do_login(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Username']").send_keys(TestData.USER_NAME)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(TestData.PASSWORD)
        self.driver.find_element(By.XPATH, "//button[contains(text(),' SIGN IN ')]").click()
        time.sleep(5)
