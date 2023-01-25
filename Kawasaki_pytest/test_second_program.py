
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()


def test_Facebook_login():

    driver.get("https://www.facebook.com/login/")
    email=driver.find_element(By.ID,"email")
    email.send_keys(("shantanukarale777@gmail.com"))
    Pass=driver.find_element(By.ID,"pass")
    Pass.send_keys(("****"))
    Button=driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
    time.sleep(5)





































































































