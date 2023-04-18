import pytest
from selenium import webdriver
from Pom.Config.config import TestData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    options.add_argument("--ignore-ssl-errors=yes")
    options.add_argument("--ignore-certificate-errors")
    options.headless=True
    # capabilities = options.capabilities
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# def setup(request, browser, url):
#     if browser == "chromium":
#         options = Options()
#         options.add_argument("--ignore-ssl-errors=yes")
#         options.add_argument("--ignore-certificate-errors")
#         capabilities = options.capabilities
#         driver = webdriver.Chrome(executable_path=TestData.Executable_Path, options=options)
#     elif browser == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     elif browser == "edge":
#         options = Options()
#         options.accept_insecure_certs = True
#         driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
#     driver.get(url)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.quit()


def pytest_addoption(parser):
    parser.addoption("--web-browser", default="chrome", help="Browser to run the tests in (chrome, firefox, edge)")
    parser.addoption("--url", default="http://localhost:8000", help="Base URL for the application being tested")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--web-browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
