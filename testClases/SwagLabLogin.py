import time

from selenium import webdriver
from pageClasses import login,home


class Test_SwagLabLogin:           #MainClass

    def test_TC1_LoginToApp_withValidDetails(self):        #test case / test method
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)

        loginObj=login.SwagLabLoginPage(driver)
        loginObj.enterUN("standard_user")
        time.sleep(2)
        loginObj.enterPWD("secret_sauce")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        time.sleep(2)

        homeObj=home.SwagLabHomePage(driver)
        actLogoText=homeObj.getActLogotext()
        expLogoText="Swag Labs"

        if actLogoText==expLogoText:
            assert True
        else:
            assert False

        time.sleep(2)
        driver.quit()

    def test_TC2_LoginToApp_withInValidDetails(self):  # test case / test method
        driver = webdriver.Edge()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)

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
            assert False

        time.sleep(2)
        driver.quit()


