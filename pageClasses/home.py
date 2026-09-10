#POM class 2
from selenium.webdriver.common.by import By


class SwagLabHomePage:

    # 1: declare webelements xpath as class variable
    logoText="//div[@class='app_logo']"
    menuOption="//button[@id='react-burger-menu-btn']"

    # 2: Initialize driver within Constructor
    def __init__(self,driver):
        self.driver=driver

    # 3: perform action on webelements within method
    def getActLogotext(self):
        actText=self.driver.find_element(By.XPATH,self.logoText).text
        return actText

    def clickOnMenuOption(self):
        self.driver.find_element(By.XPATH,self.menuOption).click()
