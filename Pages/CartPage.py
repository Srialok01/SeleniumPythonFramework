
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage():
    def __init__(self, driver):
        self.driver = driver

    CartQuantity = (By.XPATH, "//td[@class='quantity']//input[@class='qty-input']")
    Terms_And_conditions = (By.ID, "termsofservice")
    CheckoutBTN = (By.ID, "checkout")

    def cart_validation(self):
        self.driver.execute_script("window.scrollTo(0, 400);")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CartPage.Terms_And_conditions)).click()
        self.driver.find_element(*CartPage.CheckoutBTN).click()
