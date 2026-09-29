import time

import pytest
from selenium import webdriver

from Utility.CommonFunction import UtilityClass
# from Utility.customLogger import LogGen
from Utility.readProperties import ReadConfig
from pageClasses import login,home



class Test_SwagLabProduct:           #MainClass

    logger=UtilityClass.loggen()

    @pytest.mark.product1
    def test_TC3_VerifyProductName(self,setup,request):        #test case / test method
        driver=setup
        UtilityClass.loginToApp(self.logger,driver)

        homeObj=home.SwagLabHomePage(driver)
        actProductName=homeObj.getsauceLabBackpackProductName()
        expProductName=UtilityClass.readDataFromExcel(3,1)

        if actProductName==expProductName:
            self.logger.info("==Act & Exp product Name match==")
            assert True
        else:
            self.logger.info("==Act & Exp product Name mismatch==")
            UtilityClass.captureSS(driver, request.node.name)
            assert False

        time.sleep(2)
        driver.quit()



    @pytest.mark.product2
    def test_TC4_VerifyProductSize(self,setup,request):        #test case / test method
        driver=setup
        UtilityClass.loginToApp(self.logger, driver)
        homeObj=home.SwagLabHomePage(driver)
        actProductSize=homeObj.getAllProductSize()
        expProductSize=UtilityClass.readDataFromExcel(4,1)

        if actProductSize==expProductSize:
            self.logger.info("==Act & Exp product size match==")
            assert True
        else:
            self.logger.info("==Act & Exp product size mismatch==")
            UtilityClass.captureSS(driver, request.node.name)
            assert False

        time.sleep(2)
        driver.quit()

    @pytest.mark.product3
    def test_TC5_VerifyBackpackProductPrice(self,setup,request):        #test case / test method
        driver=setup
        UtilityClass.loginToApp(self.logger, driver)
        homeObj=home.SwagLabHomePage(driver)
        actProductPrice=float(homeObj.getBackpackProductPrice())
        expProductPrice=float(UtilityClass.readDataFromExcel(5,1))
        print("act--",actProductPrice)
        print("exp--",expProductPrice)
        if actProductPrice==expProductPrice:
            self.logger.info("==Act & Exp product price match==")
            assert True
        else:
            self.logger.info("==Act & Exp product price mismatch==")
            UtilityClass.captureSS(driver, request.node.name)
            assert False
        time.sleep(2)
        driver.quit()

    @pytest.mark.product4
    def test_TC5_VerifyAllProductPrice(self,setup,request):        #test case / test method
        driver=setup
        UtilityClass.loginToApp(self.logger, driver)
        homeObj=home.SwagLabHomePage(driver)
        actAllProductPrice=homeObj.getallProductPrice()
        expAllProductPrice=float(UtilityClass.readDataFromExcel(6,1))
        print("act--",actAllProductPrice)
        if actAllProductPrice==expAllProductPrice:
            self.logger.info("==Act & Exp all product price match==")
            assert True
        else:
            self.logger.info("==Act & Exp all product price mismatch==")
            UtilityClass.captureSS(driver, request.node.name)
            assert False
        time.sleep(2)
        driver.quit()


