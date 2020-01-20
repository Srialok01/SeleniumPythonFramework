import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.select import Select
from Util import Utils


class Address:
    def __init__(self, driver):
        self.driver = driver

    FirstName = (By.ID, 'BillingNewAddress_FirstName')
    LastName = (By.ID, 'BillingNewAddress_LastName')
    Email = (By.ID, 'BillingNewAddress_Email')
    Country = (By.XPATH, "//Select[@id= 'BillingNewAddress_CountryId']")
    State = (By.ID, "BillingNewAddress_StateProvinceId")
    City = (By.ID, 'BillingNewAddress_City')
    AddressLine = (By.ID, "BillingNewAddress_Address1")
    Postcode = (By.ID, 'BillingNewAddress_ZipPostalCode')
    PhoneNo = (By.ID, 'BillingNewAddress_PhoneNumber')
    BillingAddressBTN = (By.XPATH, "//div[@id='billing-buttons-container']//input")
    ShippingAddressBTN = (By.XPATH, "//input[@class='button-1 shipping-method-next-step-button']")

    def continueAddress(self):
        self.driver.find_element(*Address.BillingAddressBTN).click()
        self.driver.execute_script("window.scrollTo(0, 300);")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*Address.ShippingAddressBTN)).click()

    def SelectCountry(self):
        WebElement_Country = self.driver.find_element(*Address.Country)
        select_Country = Select(WebElement_Country)
        select_Country.select_by_value("133")

    def AddressInput(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*Address.FirstName))
        self.driver.find_element(*Address.FirstName).clear()
        self.driver.find_element(*Address.FirstName).send_keys(Utils.dict_address.get('First_Name'))
        self.driver.find_element(*Address.LastName).clear()
        self.driver.find_element(*Address.LastName).send_keys(Utils.dict_address.get('Last_Name'))
        time.sleep(2)
        email = self.driver.find_element(*Address.Email)
        scrollToEmail = email.location_once_scrolled_into_view
        email.clear()
        email.send_keys(Utils.dict_address.get('Guest_Email'))
        self.SelectCountry()
        self.driver.find_element(*Address.City).send_keys(Utils.dict_address.get('City'))
        self.driver.find_element(*Address.AddressLine).send_keys(Utils.dict_address.get('Address1'))
        self.driver.find_element(*Address.Postcode).send_keys(Utils.dict_address.get('PostCode'))
        self.driver.find_element(*Address.PhoneNo).send_keys(Utils.dict_address.get('PhoneNo'))

        BTN = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*Address.BillingAddressBTN)).click()
        # # ScrollToBtn=BTN.location_once_scrolled_into_view
        # BTN.click()
        element = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*Address.ShippingAddressBTN)).click()
        # element.click()
        # # ShipAddressContinueBTN = self.driver.find_element_by_xpath(self.)
        # # BTN=ShipAddressContinueBTN.location_once_scrolled_into_view
        # # ShipAddressContinueBTN.click()

    # def AddressInputExisting(self):
    #     # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*Address.FirstName))
    #     self.driver.execute_script("window.scrollTo(0, 400);")
    #     self.SelectCountry()
    #
    #     self.driver.find_element_by_id(self.City_id).send_keys(Utils.dict_address.get('City'))
    #     self.driver.find_element_by_id(self.Address1_id).send_keys(Utils.dict_address.get('Address1'))
    #     self.driver.find_element_by_id(self.PostCode_id).send_keys(Utils.dict_address.get('PostCode'))
    #     self.driver.find_element_by_id(self.PhoneNo_id).send_keys(Utils.dict_address.get('PhoneNo'))
    #     self.driver.find_element_by_xpath(self.BillingAddressContinueBTN_xpath).click()
    #     self.driver.find_element_by_xpath(self.ShipAddressContinueBTN_xpath).click()


""" Selecting state is not mandatory
    def SelectState(self):
        WebElement_State = self.driver.find_element_by_xpath(self.State_id)
        select_State = Select(WebElement_State)
        select_State.select_by_value(133)
"""
