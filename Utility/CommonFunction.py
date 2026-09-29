import logging
import time
from datetime import datetime
import openpyxl

from Utility.readProperties import ReadConfig
from pageClasses import login


class UtilityClass:

    @staticmethod
    def captureSS(driver, test_name):
        # Current date & time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Screenshot file name
        screenshot_path = f".\\SS\\{test_name}_{current_time}.png"

        driver.save_screenshot(screenshot_path)


    @staticmethod
    def loggen():
        # Generate filename with current date & time -> convert to string
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f".\\Logs\\SwagLabLogs{current_time}.log"  # The f stands for formatted string literal (also called an f-string)

        logging.basicConfig(filename=log_filename,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt="%Y-%m-%d %H:%M:%S",
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def readDataFromExcel(rowIndex, colIndex):
        workbook = openpyxl.load_workbook("D:\Python\Workspace\8thNov_pytestFramework\TestData\SwagLab.xlsx")
        sheet = workbook['Sheet2']

        data=sheet.cell(row=rowIndex,column=colIndex).value
        return data

    @staticmethod
    def readDataFromExcelWithSheetName(sheetName, rowIndex, colIndex):
        workbook = openpyxl.load_workbook("D:\Python\Workspace\8thNov_pytestFramework\TestData\SwagLab.xlsx")
        sheet = workbook[sheetName]

        data=sheet.cell(row=rowIndex,column=colIndex).value
        return data


    @staticmethod
    def loginToApp(logger,driver):
        loginObj = login.SwagLabLoginPage(driver)
        loginObj.enterUN(ReadConfig.getAppUN())
        logger.info("==UN Entered==")
        time.sleep(2)
        loginObj.enterPWD(ReadConfig.getAppPWD())
        logger.info("==PWD Entered==")
        time.sleep(2)
        loginObj.clickOnLoginBtn()
        logger.info("==clicked on login btn==")
        time.sleep(2)
