#POM class 2
from selenium.webdriver.common.by import By


class SwagLabHomePage:

    # 1: declare webelements xpath as class variable
    logoText="//div[@class='app_logo']"
    menuOption="//button[@id='react-burger-menu-btn']"
    sauceLabBackpackProduct="(//div[@class='inventory_item_name '])[1]"
    allProducts="//div[@class='inventory_item_name ']"
    backPackProductPrice="(//div[@class='inventory_item_price'])[1]"
    allProductPrice="//div[@class='inventory_item_price']"
    sauceLabAddToCart="(//button[text()='Add to cart'])[1]"
    cartLink="//a[@class='shopping_cart_link']"

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

    def getBackpackProductPrice(self):
        actProductPrice=self.driver.find_element(By.XPATH,self.backPackProductPrice).text  #$29.99
        actProductPrice=actProductPrice[1:]   # 29.99
        return actProductPrice

    def getallProductPrice(self):
        allProductPriceAddress=self.driver.find_elements(By.XPATH,self.allProductPrice)
        totalProductPrice=0
        for eachProductPriceAddress in allProductPriceAddress:
            price=eachProductPriceAddress.text     #$29.99 - text
            price=price[1:]                        #29.99 - text
            price=float(price)                     #29.99 - float
            totalProductPrice=totalProductPrice+price
        return totalProductPrice


    def click1stProductAddToCart(self):
        self.driver.find_element(By.XPATH,self.sauceLabAddToCart).click()

    def clickOnCartLink(self):
        self.driver.find_element(By.XPATH, self.cartLink).click()


