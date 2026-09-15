import time
from selenium import webdriver

from Utility.CommonFunction import UtilityClass
from pageClasses import login,home



class Test_SwagLabLogin:           #MainClass

    def test_TC1_LoginToApp_withValidDetails(self,setup,request):        #test case / test method
        driver=setup

        loginObj=login.SwagLabLoginPage(driver)
        loginObj.enterUN("standard_user")
        time.sleep(2)
        loginObj.enterPWD("secret_sauce")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)

        homeObj=home.SwagLabHomePage(driver)
        actLogoText=homeObj.getActLogotext()
        expLogoText="Swag Labs1"

        if actLogoText==expLogoText:
            assert True
        else:
            # UtilityClass.captureSS(driver,"test_TC1_LoginToApp_withValidDetails")
            UtilityClass.captureSS(driver, request.node.name)  # request.node.name -> get name of currently running script
            assert False

        time.sleep(2)
        driver.quit()

    def atest_TC2_LoginToApp_withInValidDetails(self,setup,request):  # test case / test method
        driver=setup
        loginObj = login.SwagLabLoginPage(driver)
        loginObj.enterUN("abc")
        time.sleep(2)
        loginObj.enterPWD("xyz")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)

        actErrorMsg=loginObj.getLoginFailedErrorMsg()
        expErrorMsg="Epic sadface: Username and password do not match any user in this service"

        if actErrorMsg==expErrorMsg:
            assert True
        else:
            # UtilityClass.captureSS(driver, "test_TC2_LoginToApp_withInValidDetails")
            UtilityClass.captureSS(driver, request.node.name)
            assert False

        time.sleep(2)
        driver.quit()


