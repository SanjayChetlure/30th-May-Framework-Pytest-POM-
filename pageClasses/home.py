#POM class 2
from selenium.webdriver.common.by import By


class SwagLabHomePage:

    # 1: declare webelements xpath as class variable
    logoText="//div[@class='app_logo']"
    menuOption="//button[@id='react-burger-menu-btn']"
    sauceLabBackpackProduct="(//div[@class='inventory_item_name '])[1]"
    allProducts="//div[@class='inventory_item_name ']"

    # 2: Initialize driver within Constructor
    def __init__(self,driver):
        self.driver=driver

    # 3: perform action on webelements within method
    def getActLogotext(self):
        actText=self.driver.find_element(By.XPATH,self.logoText).text
        return actText

    def clickOnMenuOption(self):
        self.driver.find_element(By.XPATH,self.menuOption).click()

    def getsauceLabBackpackProductName(self):
        actProductName=self.driver.find_element(By.XPATH,self.sauceLabBackpackProduct).text
        return actProductName

    def getAllProductSize(self):
        allProducts = self.driver.find_elements(By.XPATH, self.allProducts)
        allProductSize=len(allProducts)
        return allProductSize
