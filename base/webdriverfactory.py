"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import warnings

from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        warnings.simplefilter("ignore", ResourceWarning)

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        selenium_grid_url = "http://192.168.10.39:4444/wd/hub"
        baseURL = "https://letskodeit.teachable.com/"

        if self.browser:
            driver = webdriver.Remote(
                command_executor=selenium_grid_url,
                desired_capabilities={
                    'browserName': self.browser,
                    'name':"dsad",
                }
            )
        else:
            driver = webdriver.Firefox(executable_path="C:\\geckodriver")
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
