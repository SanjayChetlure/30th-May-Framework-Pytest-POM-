import time

import pytest
from selenium import webdriver

from Utility.CommonFunction import UtilityClass
# from Utility.customLogger import LogGen
from Utility.readProperties import ReadConfig
from pageClasses import login,home,yourCart,checkoutYouInfo,checkoutOverview,checkoutComplete



class Test_SwagLabProduct:           #MainClass

    logger=UtilityClass.loggen()

    @pytest.mark.product1
    def test_TC7_VerifyE2EScenario(self,setup,request):        #test case / test method
        driver=setup
        UtilityClass.loginToApp(self.logger,driver)

        homeObj=home.SwagLabHomePage(driver)
        homeObj.click1stProductAddToCart()
        time.sleep(1)
        homeObj.clickOnCartLink()
        time.sleep(1)

        youCartObj=yourCart.SwagLabYouCartPage(driver)
        youCartObj.clickOnCheckoutBtn()
        time.sleep(2)

        checkoutYouInfoObj=checkoutYouInfo.SwagLabCheckoutYouInfoPage(driver)
        checkoutYouInfoObj.enterFirstName(UtilityClass.readDataFromExcel(7,1))
        time.sleep(1)
        checkoutYouInfoObj.enterLastName(UtilityClass.readDataFromExcel(7,2))
        time.sleep(1)
        checkoutYouInfoObj.enterPostalCode(UtilityClass.readDataFromExcel(7,3))
        time.sleep(1)
        checkoutYouInfoObj.clickOnContinueBtn()
        time.sleep(1)

        checkoutOverviewObj=checkoutOverview.SwagLabCheckoutOverviewPage(driver)
        checkoutOverviewObj.clickOnFinishBtn()
        time.sleep(1)

        checkoutCompleteObj=checkoutComplete.SwagLabCheckoutCompletePage(driver)
        actOrderPlacedMsg=checkoutCompleteObj.getOrderPlacedMessage()
        expOrderPlacedMsg=UtilityClass.readDataFromExcel(7,4)
        time.sleep(1)

        if actOrderPlacedMsg==expOrderPlacedMsg:
            self.logger.info("==Act & Exp order placed message match==")
            assert True
        else:
            self.logger.info("==Act & Exp order placed message mismatch==")
            UtilityClass.captureSS(driver, request.node.name)
            assert False

        time.sleep(2)
        driver.quit()


