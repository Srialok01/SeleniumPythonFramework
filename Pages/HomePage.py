from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    Electronics = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Electronics ')]")
    Cellphone = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Cell phones')]")
    Others = (By.XPATH, "//ul[@class='top-menu notmobile']//a[contains(text(),'Others')]")

    def Hover(self):
        hoverElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomePage.Electronics))
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()

    def NavigateToCellPhone(self):
        self.Hover()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomePage.Cellphone)).click()
        time.sleep(2)

    def NavigateToOthers(self):
        self.Hover()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*HomePage.Others)).click()
        time.sleep(2)
