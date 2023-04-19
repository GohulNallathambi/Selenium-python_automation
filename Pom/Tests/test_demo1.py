# import time
# import pytest
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @pytest.mark.usefixtures("setup")
# class TestWaitsDemo:
#
#     def test_explicit_demo(self):
#
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
#         all_dates = self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper' ]//tbody//td[@class!='inActiveTD']"))) \
#             .find_elements(By.XPATH, "//div[@id='monthWrapper' ]//tbody//td[@class!='inActiveTD']")
#         print(all_dates)
#         for date in all_dates:
#             if date.get_attribute("data-date") == "09/03/2023":
#                 date.click()
#                 break
#         self.driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
#
#     def test_implicit_demo(self):
#         self.driver.implicitly_wait(5)
#
#         self.driver.switch_to.frame("iframeResult")
#         time.sleep(5)
#         self.wait.until(EC.alert_is_present())
#         alet = self.driver.switch_to.alert
#         time.sleep(5)
#         alet.accept()
#         self.driver.find_element("//a[@id = 'webklipper-publisher-widget-container-notification-close-div']/i").click()
#         self.driver.find_element("//form/button[@id='~25b5c3de']").click()
#         depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
#         depart_from.click()
#         depart_from.send_keys("Mumbai")
#         time.sleep(2)
#         depart_from.send_keys(Keys.ENTER)
#         going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
#         going_to.click()
#         going_to.send_keys("New York")
#         time.sleep(2)
#         search_results = self.driver.find_elements(By.XPATH, "//div[@class='viewport']/div/div/li")
#         print(len(search_results))
#         for results in search_results:
#             print(results.text)
#             if "New York (JFK)" in results.text:
#                 results.click()
#                 break
#
