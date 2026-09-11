import pytest
from selenium import webdriver

@pytest.fixture
def setup():
   driver=webdriver.Edge()
   driver.maximize_window()
   driver.get("https://www.saucedemo.com/")
   driver.implicitly_wait(5)
   return driver
