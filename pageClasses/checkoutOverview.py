from selenium.webdriver.common.by import By


class SwagLabCheckoutOverviewPage:

    checkout="//button[text()='Finish']"


    def __init__(self, driver):
        self.driver = driver


    def clickOnFinishBtn(self):
        self.driver.find_element(By.XPATH, self.checkout).click()
