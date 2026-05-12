# from selenium import webdriver
# from selenium.webdriver.common.by import By



# class Login:
#     username_xpath = "//input[@placeholder='Username']"
#     password_xpath = "//input[@placeholder='Password']"
#     login_xpath = "//button[normalize-space()='Login']"

#     def __init__(self, driver):
#         self.driver = driver
    
#     def set_username(self,username):
#         self.driver.find_element(By.XPATH, self.username_xpath).clear()
#         self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)
#         return username
    
#     def set_password(self,password):
#         self.driver.find_element(By.XPATH, self.password_xpath).clear()
#         self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
#         return password

#     def click_login(self):
#         self.driver.find_element(By.XPATH,self.login_xpath).click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:

    username_xpath = "//input[@placeholder='Username']"
    password_xpath = "//input[@placeholder='Password']"
    login_xpath = "//button[normalize-space()='Login']"
    

    def __init__(self, driver):
        self.driver = driver
        
    def set_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_xpath))
        )
        username_field.clear()
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.password_xpath)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()