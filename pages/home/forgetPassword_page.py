from time import sleep

from base.basepage import BasePage
import logging

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPages

_forgetPassword = "input[class*='email']";


class ForgetPasswordPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    _forgetPassword = "input[class*='email']";
    _forgetPassword_btn = "input[type='submit']";
    _error_Notification = "span[class*='help-block']";

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPages(driver)

    def resetPassword(self, email):
        self.sendKeys(email, _forgetPassword, locatorType="css")
        self.click(self._forgetPassword_btn, locatorType="css")

    def verifyResetPasswordFail(self):
        result = self.verifyText("We couldn't find an account with that email address",
                                 self.getText(self._error_Notification, locatorType="css"))
        return result
