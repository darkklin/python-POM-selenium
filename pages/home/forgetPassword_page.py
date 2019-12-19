from base.basepage import BasePage
import logging

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPages


_forgetPassword= "input[class*='email']";

class ForgetPassword(BasePage):
    log = cl.customLogger(logging.DEBUG)

    _forgetPassword = "input[class*='email']";

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPages(driver)

    def resetPassword(self,email):
        self.sendKeys(email,_forgetPassword,locatorType="css")

    def verifyTitle(self):
        return self.verifyText("Reset Passworddsadasd")
