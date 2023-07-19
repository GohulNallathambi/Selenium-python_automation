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
        

    def host_click(self, name):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Hosts')]").click()
        time.sleep(3)
        search =self.driver.find_element(By.XPATH, "//input[@name='search']")
        search.click()
        search.send_keys(name)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

    def host_alert(self):
        self.driver.find_element(By.XPATH, "//div[@class='row']/div[3]/div/a/div/div/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//*[contains(text(),'Results per page:')]/select/option[4]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//thead/tr[1]/th[1]/input[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//th[contains(text(),'Resolve')]").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, " //body/app-root[1]/app-global[1]/div[1]/app-alerts[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/label[2]/span[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//textarea").send_keys("Legitimate")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]").click()
        time.sleep(3)


        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//*[@id='Management']/a/span[2]").click()
        #
        # page = self.driver.find_element(By.XPATH, "//span[contains(text(),'VT Settings')]")
        #
        # self.driver.execute_script("arguments[0].scrollIntoView();", page)
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'VT Settings')]").click()
        # time.sleep(2)

