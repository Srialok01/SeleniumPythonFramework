import moment
from Util import Utils
import allure


class SS(object):
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, path):
        directory = "Screenshots"
        # time = moment.now().strftime("%H-%M-%S_%m-%d-%y")
        # testName = Util.whoami()
        # ScreenShotName = testName + time
        # allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
        #               attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file(directory+path)

    def snapshot(self):
        time = moment.now().strftime("%H-%M-%S_%m-%d-%y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        return ScreenShotName.png
