import time
from selenium import webdriver
from selenium .webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
def text_box():
    driver.get('https://demoqa.com/text-box')
    name = driver.find_element(By.ID, 'userName')
    name.send_keys('Ajay devgan')
    Email = driver.find_element(By.ID, 'userEmail')
    Email.send_keys('ajaydevgan@gmail.com')
    Adress = driver.find_element(By.ID, 'currentAddress')
    Adress.send_keys('East bandra mumbai')
    time.sleep(5)

text_box()




































































































































































































































































































































