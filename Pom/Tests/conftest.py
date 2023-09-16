import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdrivermanager import EdgeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="class")
# def setup(request):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--ignore-certificate-errors")
#     capabilities = options.to_capabilities()
#     capabilities['acceptInsecureCerts'] = True
#     driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), desired_capabilities=capabilities)
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()

def setup(request, browser, url):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.accept_insecure_certs = True
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        options = Options
        options.accept_insecure_certs = True
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--web-browser", default="chrome", help="Browser to run the tests in (chrome, firefox, edge)")
    parser.addoption("--url", default="http://localhost:8080", help="Base URL for the application being tested")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--web-browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
