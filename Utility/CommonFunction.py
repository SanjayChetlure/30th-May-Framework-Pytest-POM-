import logging
import time
from datetime import datetime
import openpyxl
from selenium.common import NoAlertPresentException
from selenium.webdriver.support.select import Select

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

    """
    Handles alert popups.
    :param driver: WebDriver instance
    :param action: Action to perform on the alert ('accept', 'dismiss', 'text')
    :return: Text of the alert (if action is 'text'), otherwise None
    """
    @staticmethod
    def handle_alert(driver, action="accept"):
        try:
            alert = driver.switch_to.alert
            if action == "accept":
                alert.accept()
            elif action == "dismiss":
                alert.dismiss()
            elif action == "text":
                return alert.text
            else:
                raise ValueError("Invalid action. Use 'accept', 'dismiss', or 'text'.")
        except NoAlertPresentException:
            print("No alert present.")
            return None

    """
    Handles a listbox using select_by_index, select_by_value, or select_by_visible_text.
    :param element: WebElement of the listbox
    :param action: Action to perform ('index', 'value', 'text')
    :param value: Value to use for the action (index as int, value as str, or visible text as str)
    """
    @staticmethod
    def handle_listbox(element, action, value=None):
        action=action.lower()
        select = Select(element)
        if action == "index":
            if isinstance(value, int):
                select.select_by_index(value)
            else:
                raise ValueError("For 'index', value must be an integer.")
        elif action == "value":
            if isinstance(value, str):
                select.select_by_value(value)
            else:
                raise ValueError("For 'value', value must be a string.")
        elif action == "text":
            if isinstance(value, str):
                select.select_by_visible_text(value)
            else:
                raise ValueError("For 'text', value must be a string.")
        else:
            raise ValueError("Invalid action. Use 'index', 'value', or 'text'.")

    """
    Switches to an iframe using index, WebElement, or id/name.
    :param driver: WebDriver instance
    :param identifier: Can be an index (int), WebElement, or id/name (str)
    """
    @staticmethod
    def switch_to_iframe(driver, identifier):
        try:
            if isinstance(identifier, int):
                driver.switch_to.frame(identifier)
            elif hasattr(identifier, 'tag_name'):  # Check if it's a WebElement
                driver.switch_to.frame(identifier)
            elif isinstance(identifier, str):
                driver.switch_to.frame(identifier)
            else:
                raise ValueError("Invalid identifier. Use an index (int), WebElement, or id/name (str).")
        except Exception as e:
            print(f"Error switching to iframe: {e}")

    """
    Handles child window popups.
    :param driver: WebDriver instance
    :param action: Action to perform ('switch_to_child','switch_back', 'close', 'get_title')
    :return: Title of the child window (if action is 'get_title'), otherwise None
    """
    @staticmethod
    def handle_child_window(driver, action="switch_back"):
        parent_window = driver.current_window_handle
        all_windows = driver.window_handles

        for window in all_windows:
            if window != parent_window:
                if action == "switch_to_child":
                    driver.switch_to.window(window)
                elif action == "close":
                    driver.switch_to.window(window)
                    driver.close()
                    driver.switch_to.window(parent_window)
                elif action == "get_title":
                    driver.switch_to.window(window)
                    title = driver.title
                    driver.switch_to.window(parent_window)
                    return title
                elif action == "switch_back":
                    driver.switch_to.window(parent_window)
                else:
                    raise ValueError("Invalid action. Use 'switch_to_child', 'switch_back', 'close', or 'get_title'.")
                break