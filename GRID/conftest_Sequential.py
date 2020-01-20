from pytest import fixture
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from selenium import webdriver


# @fixture(params=["safari"], scope="class")


@fixture(params=["safari"], scope="class")
def test_setup_safari(request):
    capabilities = {
        'browserName': 'safari',
        'browserVersion': 'latest-1',
        'platformName': 'macOS 10.13',
        'sauce:options': {
        }
    }
    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]

    driver = webdriver.Remote(
        command_executor='https://{}:{}@ondemand.saucelabs.com:443/wd/hub'.format(username, access_key),
        desired_capabilities=capabilities)

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    print("Test completed---SAFARI")


@fixture(params=["chrome"], scope="class")
def test_setup(request):
    from selenium import webdriver

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    print("Test completed--chrome")


@fixture(params=["firefox"], scope="class")
def test_setup_firefox(request):
    from selenium import webdriver

    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              desired_capabilities={'browserName': 'firefox'})

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    print("Test completed--firefox")
