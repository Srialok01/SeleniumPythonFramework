from pytest import fixture
import os
from selenium import webdriver
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.


# @fixture(params=["safari"], scope="class")
@fixture(params=["chrome", "safari2", "firefox"], scope="class")
def test_setup(request):
    global driver

    desired_cap = {
        'platform': "Mac OS X 10.13",
        'browserName': "safari",
        'version': "11.1",
        'build': "Zalenium GRID",
        'name': "Sauce Labs-Safari",
    }
    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]

    if request.param == "safari":
        driver = webdriver.Remote(
            command_executor='https://{}:{}@ondemand.saucelabs.com:443/wd/hub'.format(username, access_key),
            desired_capabilities=desired_cap)

    if request.param == "chrome":
        # Local webdriver implementation
        # web_driver = webdriver.Chrome()
        # Remote WebDriver implementation
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})

    if request.param == "firefox":
        # Local webdriver implementation
        # web_driver = webdriver.Firefox()
        # Remote WebDriver implementation
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox'})

    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield
    driver.close()
    print("Test completed")
