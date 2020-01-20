import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="E:/Automation Frameworks/Selenium_Python_Framework/Drivers"
                                                  "/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="E:/Automation Frameworks/Selenium_Python_Framework/Drivers"
                                                   "/geckodriver.exe")
    driver.implicitly_wait(3)
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")


def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        return ["###############################################################"
                " RUNNING TESTS IN VERBOSE MODE#################################################"]
