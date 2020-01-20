import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Util import Utils


class Payment:
    def __init__(self, driver):
        self.driver = driver

    CreditCardRadioBTN = (By.ID, "paymentmethod_1")
    PaymentContinueBTN = (By.XPATH, "//input[@type='button'][@class='button-1 payment-method-next-step-button']")
    CardHolderName = (By.ID, "CardholderName")
    CardNumber = (By.ID, "CardNumber")
    ExpirationMonth = (By.XPATH, "//select[@id='ExpireMonth']")
    ExpirationYear = (By.XPATH, "//select[@id='ExpireYear']")
    CVV = (By.XPATH, "//input[@id='CardCode']")
    CardContinueBTN = (By.XPATH, "//input[@class='button-1 payment-info-next-step-button']")

    def PaymentOptions(self):
        self.driver.execute_script("window.scrollTo(0, 300);")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*Payment.CreditCardRadioBTN)).click()

        self.driver.find_element(*Payment.PaymentContinueBTN).click()

        self.driver.find_element(*Payment.CardHolderName).send_keys(Utils.CardHolderName)
        self.driver.find_element(*Payment.CardNumber).send_keys(Utils.CardNo)
        WebElement_Month = self.driver.find_element(*Payment.ExpirationMonth)

        select_Expdate = Select(WebElement_Month)
        select_Expdate.select_by_index(6)
        WebElement_Year = self.driver.find_element(*Payment.ExpirationYear)
        select_ExpYear = Select(WebElement_Year)
        select_ExpYear.select_by_index(5)
        self.driver.find_element(*Payment.CVV).send_keys(Utils.cvv)
        self.driver.find_element(*Payment.CardContinueBTN).click()
