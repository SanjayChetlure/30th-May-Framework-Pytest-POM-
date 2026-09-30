from selenium.webdriver.common.by import By


class SwagLabYouCartPage:

    checkout="//button[text()='Checkout']"

    # 2: Initialize driver within Constructor
    def __init__(self,driver):
        self.driver=driver


    def clickOnCheckoutBtn(self):
        self.driver.find_element(By.XPATH,self.checkout).click()