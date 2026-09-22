import pytest
from selenium import webdriver
from Utility.readProperties import ReadConfig


@pytest.fixture
def setup(browser):
   driver=initializeBrowser(browser)
   driver.maximize_window()
   driver.get(ReadConfig.getAppURL())
   driver.implicitly_wait(5)
   return driver


def initializeBrowser(browser):
   if browser=="chrome":
      driver = webdriver.Chrome()
      return driver
   elif browser=="firefox":
      driver=webdriver.Firefox()
      return driver
   elif browser=="edge":
      driver=webdriver.Edge()
      return driver


#use to set default browserName
def pytest_addoption(parser):
   parser.addoption("--browser", action="store", default="edge")


#this code is use to get browser value from cmd
@pytest.fixture()
def browser(request):
  return request.config.getoption("--browser")


#1: It is hook for adding environment info into Report (customize info in report)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
   metadata['Project Name'] = 'Swag Labs'
   metadata['Module Name'] = 'Login'
   metadata['Automation Tester Name'] = 'Sanjay'



