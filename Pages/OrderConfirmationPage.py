import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OrderConfirmation():
    def __init__(self, driver):
        self.driver = driver

    ConfirmBTN = (By.XPATH, "//input[@class='button-1 confirm-order-next-step-button']")
    Order_No = (By.XPATH, "//div[@class='order-number']/strong")

    def OrderConfirmationdetails(self):
        self.driver.execute_script("window.scrollTo(0, 800);")
        self.driver.find_element(*OrderConfirmation.ConfirmBTN).click()
        OrderNo = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*OrderConfirmation.Order_No)).text
        print(OrderNo)
        text_file = open('C:/files/file.txt', 'a')
        text_file.writelines("\n" + OrderNo)
        text_file.close()
