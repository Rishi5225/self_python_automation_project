from selenium import webdriver
from selenium.webdriver.common.by import By



class Login:
    username_xpath = "//input[@id='user-name']"
    password_xpath = "//input[@id='password']"
    login_xpath = "//input[@id='login-button']"

    def __init__(self, driver):
        self.driver = driver
    
    def set_username(self,username):
        self.driver.find_element(By.XPATH, self.username_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)
        return username
    
    def set_password(self,password):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)
        return password

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_xpath).click()