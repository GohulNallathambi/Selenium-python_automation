# import pytest
# from Pom.Pages.host import HostPage
# from Pom.Pages.login import LoginPage
#
#
# @pytest.mark.usefixtures('setup')
# class TestWaitsDemo2:
#     @pytest.fixture(autouse=True)
#     def myfixture(self, driver):
#         self.login = LoginPage(driver)
#         self.host = HostPage(driver)
#     def test_page(self):
#         self.login.test_do_login()
#         self.login.scroll_down()
#         self.host.host_click(name="Gohul")
#
#
