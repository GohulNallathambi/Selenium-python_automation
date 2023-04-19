import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pom.Base.Base_driver import BaseDriver
from Pom.Config.config import TestData


class HostPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    def host_click(self, name):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Hosts')]").click()
        time.sleep(3)
        search =self.driver.find_element(By.XPATH, "//input[@name='search']")
        search.click()
        search.send_keys(name)
        search.send_keys(Keys.ENTER)
        time.sleep(2)


        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//*[@id='Management']/a/span[2]").click()
        #
        # page = self.driver.find_element(By.XPATH, "//span[contains(text(),'VT Settings')]")
        #
        # self.driver.execute_script("arguments[0].scrollIntoView();", page)
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'VT Settings')]").click()
        # time.sleep(2)

