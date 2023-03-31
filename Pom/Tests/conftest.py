import pytest
from selenium import webdriver
from Pom.Config.config import TestData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
# def setup(request):
#     chrome_options = Options()
#     chrome_options.add_argument('--ignore-certificate-errors')
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()
def setup(request, browser, url):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    if browser == "chromium":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        options = Options()
        options.accept_insecure_certs = True
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--web-browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--web-browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
