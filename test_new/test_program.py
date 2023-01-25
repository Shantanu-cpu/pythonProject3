


def test_one():
     x=10
     y=20
     assert x==y

def test_one_1():
     x=10
     y=10
     assert x==y


import time
from selenium import webdriver
from selenium .webdriver.common.by import By
import pytest

class New:
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/login/")
        User_name = driver.find_element(By.ID, "email")
        User_name.send_keys(input("Enter user name: "))
        Pass = driver.find_element(By.ID, "pass")
        Pass.send_keys(input("Enter password: "))
        Button = driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
        time.sleep(10)






new=New()
new.test_login()












