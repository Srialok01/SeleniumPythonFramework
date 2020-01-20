
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/aloks/PycharmProjects/Automation Projects/Drivers/chromedriver.exe")

driver.get('https://demo.nopcommerce.com/onepagecheckout')
abc =driver.title

print(abc)
driver.quit()