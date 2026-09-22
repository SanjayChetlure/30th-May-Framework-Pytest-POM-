import time
from selenium import webdriver

from Utility.CommonFunction import UtilityClass
# from Utility.customLogger import LogGen
from Utility.readProperties import ReadConfig
from pageClasses import login,home



class Test_SwagLabLogin:           #MainClass

    logger=UtilityClass.loggen()

    def test_TC1_LoginToApp_withValidDetails(self,setup,request):        #test case / test method
        driver=setup
        loginObj=login.SwagLabLoginPage(driver)
        loginObj.enterUN(ReadConfig.getAppUN())
        self.logger.info("==UN Entered==")
        time.sleep(2)
        loginObj.enterPWD(ReadConfig.getAppPWD())
        self.logger.info("==PWD Entered==")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        self.logger.info("==clicked on login btn==")
        time.sleep(2)

        homeObj=home.SwagLabHomePage(driver)
        actLogoText=homeObj.getActLogotext()
        expLogoText="Swag Labs"

        if actLogoText==expLogoText:
            self.logger.info("==Act & Exp Logo text match==")
            assert True
        else:
            self.logger.info("==Act & Exp Logo text mismatch==")
            UtilityClass.captureSS(driver, request.node.name)  # request.node.name -> get name of currently running script
            assert False

        time.sleep(2)
        driver.quit()


    def test_TC2_LoginToApp_withInValidDetails(self,setup,request):        #test case / test method
        driver=setup
        loginObj=login.SwagLabLoginPage(driver)
        loginObj.enterUN(ReadConfig.getINIFileData("Invalid App Credentials","InvalidUN"))
        self.logger.info("== Invalid UN Entered==")
        time.sleep(2)
        loginObj.enterPWD(ReadConfig.getINIFileData("Invalid App Credentials","InvalidPWD"))
        self.logger.info("==Invalid PWD Entered==")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        self.logger.info("==clicked on login btn==")
        time.sleep(2)

        actErrorMsg = loginObj.getLoginFailedErrorMsg()
        expErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actErrorMsg == expErrorMsg:
            self.logger.info("==Act & Exp Error Msg match==")
            assert True
        else:
            self.logger.info("==Act & Exp Error Msg mismatch==")
            UtilityClass.captureSS(driver, request.node.name)
            assert False

        time.sleep(2)
        driver.quit()




