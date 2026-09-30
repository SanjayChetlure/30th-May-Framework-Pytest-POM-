from selenium.webdriver.common.by import By


class SwagLabCheckoutCompletePage:

    orderSuccessMsg="//h2[@class='complete-header']"


    def __init__(self, driver):
        self.driver = driver


    def getOrderPlacedMessage(self):
        actOrderPlacedmsg=self.driver.find_element(By.XPATH, self.orderSuccessMsg).text
        return actOrderPlacedmsg
