
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OtherItems:
    def __init__(self, driver):
        self.driver = driver

    SoundSpeaker = (By.LINK_TEXT, "Portable Sound Speakers")
    AddToCart = (By.XPATH, "//input[@id='add-to-cart-button-23']")
    ShoppingCart = (By.XPATH, "//div[@class='header-links']//descendant::span[@class ='cart-label']")
    ShoppingCart_Confirmation = (By.XPATH, "//div[@id='bar-notification']//span")
    GoToCart = (By.XPATH, "//div[@class='buttons']/input[@value='Go to cart']")

    def SelectSpeakers(self):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*OtherItems.SoundSpeaker)).click()
        self.driver.execute_script("window.scrollTo(0, 400);")
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*OtherItems.AddToCart)).click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*OtherItems.ShoppingCart_Confirmation)).click()
        self.driver.execute_script("window.scrollTo(0, -300);")
        self.Hover()

    def Hover(self):
        hoverElement = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*OtherItems.ShoppingCart))
        hover = ActionChains(self.driver)
        hover.move_to_element(hoverElement).perform()
        self.driver.find_element(*OtherItems.GoToCart).click()
