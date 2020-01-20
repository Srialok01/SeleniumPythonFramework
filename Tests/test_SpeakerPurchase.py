import allure
import moment
import pytest

from Util import Utils
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.Electronics_OthersPage import OtherItems
from Pages.LoginPage import LoginPage

from Pages.AddressPage import Address
from Pages.PaymentPage import Payment
from Pages.OrderConfirmationPage import OrderConfirmation
from Util.SS import SS
from Util.Utils import URL


# @pytest.mark.skip(" I don't want to execute this now")


@pytest.mark.usefixtures('test_setup')
class Test_SpeakerPurchase():
    global ss_path
    ss_path = '/SpeakerPurchaseNewCustomer/'

    def test_01HomePage(self):

        driver = self.driver
        self.driver.get(URL)

        homeObj = HomePage(driver)
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)
        homeObj.NavigateToOthers()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_02Speaker_buy(self):
        driver = self.driver
        cellObj = OtherItems(driver)
        cellObj.SelectSpeakers()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_03Cart_validations(self):
        driver = self.driver
        cartObj = CartPage(driver)
        cartObj.cart_validation()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)
        # title_PhonePage = driver.title
        # assert title_PhonePage == 'nopCommerce demo store. Checkout', 'Page not loaded'

    def test_04Login(self):
        driver = self.driver
        loginObj = LoginPage(driver)
        loginObj.Checkout_as_Guest()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_05Address(self):
        driver = self.driver
        addressObj = Address(driver)
        addressObj.AddressInput()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)
        title_PhonePage = driver.title
        assert title_PhonePage == 'nopCommerce demo store. Checkout', 'Page not loaded'

    def test_06Payment(self):
        driver = self.driver
        paymentObj = Payment(driver)
        paymentObj.PaymentOptions()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)

    def test_07OrderConfirmation(self):
        driver = self.driver
        orderConfObj = OrderConfirmation(driver)
        orderConfObj.OrderConfirmationdetails()
        ss = SS(driver)
        time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
        testName = Utils.whoami()
        ScreenShotName = testName + time
        ss.screenshot(ss_path + ScreenShotName + ".png")
        allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                      attachment_type=allure.attachment_type.PNG)
