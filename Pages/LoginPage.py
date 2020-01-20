import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Util import Utils


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    Email = (By.ID, "Email")
    Password = (By.ID, "Password")
    LoginButton = (By.XPATH, "//input[@class ='button-1 login-button']")
    CheckOutAsGuest_BTN = (By.XPATH, "//input[@class ='button-1 checkout-as-guest-button']")

    def Login(self):
        time.sleep(3)
        email = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*LoginPage.Email))
        ScrollToEmail = email.location_once_scrolled_into_view
        email.send_keys(Utils.Email)

        self.driver.find_element(*LoginPage.Password).send_keys(Utils.Password)
        self.driver.find_element(*LoginPage.LoginButton).click()

    def Checkout_as_Guest(self):
        self.driver.find_element(*LoginPage.CheckOutAsGuest_BTN).click()
