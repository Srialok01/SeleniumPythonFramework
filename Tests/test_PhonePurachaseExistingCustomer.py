import allure
import moment
import pytest

from Util import SS, Utils
from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Pages.Electronics_CellPhonePage import CellPhonePage
from Pages.LoginPage import LoginPage
from Pages.CheckOutPage import CheckOut
from Pages.AddressPage import Address
from Pages.PaymentPage import Payment
from Pages.OrderConfirmationPage import OrderConfirmation
from Util.SS import SS


#@pytest.mark.skip("I don't want to execute this now")
@pytest.mark.usefixtures('test_setup')
class Test_PhonePurchaseExistingCustomer:
    try:
        global ss_path
        ss_path = '/PhonePurchaseExistingCustomer/'

        def test_01HomePage(self):

            homeObj = HomePage(self.driver)
            homeObj.NavigateToCellPhone()
            ss = SS(self.driver)
            time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)

        def test_02Phone_buy(self):
            driver = self.driver
            cellObj = CellPhonePage(driver)
            cellObj.SelectPhone()
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)
            title_PhonePage = driver.title
            assert title_PhonePage == 'nopCommerce demo store. Shopping Cart', 'Page not loaded'

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
            title_PhonePage = driver.title
            assert title_PhonePage == 'nopCommerce demo store. Login', 'Page not loaded'

        def test_04Login(self):
            driver = self.driver
            loginObj = LoginPage(driver)
            loginObj.Login()
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)
            title_PhonePage = driver.title
            assert title_PhonePage == 'nopCommerce demo store. Shopping Cart', 'Page not loaded'

        def test_05Checkout(self):
            driver = self.driver
            checkoutObj = CheckOut(driver)
            checkoutObj.Check_out()
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)
            ss.screenshot(ss_path + ScreenShotName + ".png")

        def test_06Address(self):
            driver = self.driver
            addressObj = Address(driver)
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)
            addressObj.continueAddress()
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)

        def test_07Payment(self):
            driver = self.driver
            paymentObj = Payment(driver)
            paymentObj.PaymentOptions()
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%m-%d-%y")
            testName = Utils.whoami()
            ScreenShotName = testName + time

            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)

        def test_08OrderConfirmation(self):
            driver = self.driver
            orderConfObj = OrderConfirmation(driver)
            orderConfObj.OrderConfirmationdetails()
            ss = SS(driver)
            time = moment.now().strftime("%H-%M-%S_%m-%d-%y")
            testName = Utils.whoami()
            ScreenShotName = testName + time
            ss.screenshot(ss_path + ScreenShotName + ".png")
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenShotName,
                          attachment_type=allure.attachment_type.PNG)

    except AssertionError as error:
        print(error)
