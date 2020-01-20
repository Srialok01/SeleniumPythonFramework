from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CellPhonePage():
    def __init__(self, driver):
        self.driver = driver

    NokiaPhone = (By.LINK_TEXT, "Nokia Lumia 1020")
    AddToCartBTN = (By.XPATH, "//input[@type='button'][@id='add-to-cart-button-20']")
    ShoppingCart = (By.XPATH, "//div[@class='header-links']//descendant::span[@class ='cart-label']")
    ShoppingCart_Confirmation = (By.XPATH, "//div[@id='bar-notification']//span")
    GoToCart = (By.XPATH, "//div[@class='buttons']/input[@value='Go to cart']")

    def SelectPhone(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CellPhonePage.NokiaPhone)).click()
        self.driver.execute_script("window.scrollTo(0, 300);")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CellPhonePage.AddToCartBTN)).click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CellPhonePage.ShoppingCart_Confirmation)).click()
        self.driver.execute_script("window.scrollTo(0, -300);")
        self.Hover()

    def Hover(self):
        hoverElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*CellPhonePage.ShoppingCart))
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()
        self.driver.find_element(*CellPhonePage.GoToCart).click()
