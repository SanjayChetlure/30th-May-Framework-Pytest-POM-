
#POM class 1
from selenium.webdriver.common.by import By


class SwagLabLoginPage:

    #1: declare webelements xpath as class variable
    username="(//input[@class='input_error form_input'])[1]"
    password="//input[@name='password']"
    login="//input[@name='login-button']"
    errorMsg="//h3[contains(text(),'Username and password do not match')]"


    #2: Initialize driver within Constructor
    def __init__(self,driver):
        self.driver=driver        #instanceVariable=localVariable


    #3: perform action on webelements within method
    def enterUN(self,UnValue):
        self.driver.find_element(By.XPATH,self.username).send_keys(UnValue)

    def enterPWD(self,pwdValue):
        self.driver.find_element(By.XPATH, self.password).send_keys(pwdValue)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH,self.login).click()

    def getLoginFailedErrorMsg(self):
        actErrorMsg=self.driver.find_element(By.XPATH,self.errorMsg).text
        return actErrorMsg


