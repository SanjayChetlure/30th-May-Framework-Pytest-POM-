import time

import pytest
from selenium import webdriver

from Utility.CommonFunction import UtilityClass
# from Utility.customLogger import LogGen
from Utility.readProperties import ReadConfig
from pageClasses import login,home



class Test_SwagLabProduct:           #MainClass

    logger=UtilityClass.loggen()

    def loginToApp(self,driver):
        loginObj = login.SwagLabLoginPage(driver)
        loginObj.enterUN(ReadConfig.getAppUN())
        self.logger.info("==UN Entered==")
        time.sleep(2)
        loginObj.enterPWD(ReadConfig.getAppPWD())
        self.logger.info("==PWD Entered==")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        self.logger.info("==clicked on login btn==")
        time.sleep(2)

    @pytest.mark.product1
    def test_TC3_VerifyProductName(self,setup,request):        #test case / test method
        driver=setup
        self.loginToApp(driver)

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
    def test_TC4_VerifyProductPrice(self,setup,request):        #test case / test method
        driver=setup
        self.loginToApp(driver)

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


