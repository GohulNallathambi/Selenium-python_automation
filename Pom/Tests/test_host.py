import pytest
import softest as softest
from Pom.Pages.host import HostPage
from Pom.Pages.login import LoginPage
# from ddt import ddt, data, unpack


@pytest.mark.usefixtures('setup')
class Test_Host:

    def test_log(self):
        host = HostPage(self.driver)
        login = LoginPage(self.driver)
        login.test_do_login()
        host.host_alert()
