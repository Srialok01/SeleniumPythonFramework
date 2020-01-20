import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CheckOut():
    def __init__(self, driver):
        self.driver = driver

    Terms_And_conditions = (By.ID, "termsofservice")
    CheckoutBTN = (By.ID, "checkout")


    def Check_out(self):
        self.driver.execute_script("window.scrollTo(0, 400);")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CheckOut.Terms_And_conditions)).click()
        self.driver.find_element(*CheckOut.CheckoutBTN).click()
