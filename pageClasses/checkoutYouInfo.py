from selenium.webdriver.common.by import By


class SwagLabCheckoutYouInfoPage:

    firstName="//input[@name='firstName']"
    lastName="//input[@name='lastName']"
    postalCode="//input[@name='postalCode']"
    continueBtn="//input[@name='continue']"

    def __init__(self, driver):
        self.driver = driver


    def enterFirstName(self,fnValue):
        self.driver.find_element(By.XPATH,self.firstName).send_keys(fnValue)

    def enterLastName(self,lnValue):
        self.driver.find_element(By.XPATH,self.lastName).send_keys(lnValue)

    def enterPostalCode(self, pcValue):
        self.driver.find_element(By.XPATH, self.postalCode).send_keys(pcValue)

    def clickOnContinueBtn(self):
        self.driver.find_element(By.XPATH, self.continueBtn).click()
