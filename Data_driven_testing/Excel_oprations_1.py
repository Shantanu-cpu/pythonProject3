# import openpyxl
# import time
# from selenium import webdriver
# from selenium .webdriver.common.by import By
# from Utiles import Form
# driver=webdriver.Chrome()
# driver.get('https://demoqa.com/automation-practice-form')
#
# path="D:\STLC\new_automation.xlsx"
#
# sheet='Sheet1'
# row=Form.row(path,sheet)
# for i in range(2,row+1):
#     name=Form.read(path,'new_automation',sheet,i,2)


# import Utilies
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.facebook.com/")
# path = "D:\STLC\new_automation.xlsx"
# rows = Utilies.get_no_rows(path, 'facebook')
#
# for i in range(2, rows+1):
#     username = Utilies.read_data(path, 'facebook', i, 1)
#     password = Utilies.read_data(path, 'facebook', i, 2)
#     email = driver.find_element(By.ID, "email")
#     email.send_keys(username)
#     driver.find_element(By.ID, "pass").send_keys(password)
#     driver.find_element(By.NAME, "login").click()
#     if driver.title == "Facebook – log in or sign up":
#         print("Test Case is Passed...")
#         Utilies.write_data(path, 'DDT', i, 3, "Passed")
#     else:
#         print("Test Case is Failed...")
#         Utilies.write_data(path, 'DDT', i, 3, "Failed")
#     driver.find_element(By.LINK_TEXT, "m.facebook").click()












































































