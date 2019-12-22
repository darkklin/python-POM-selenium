import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
# from utilities.util import Util
from utilities import util
from utilities.util import Util


class NavigationPages(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # ut = Util.verifyTextMatch()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    # Locators
    _logo = "a[class*='logo']"
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _log_out = "a[href*='out']"
    _icon = "img[class='gravatar']"
    _login_link = "Login"
    _forgot_Password = "Forgot Password?"
    _page_title = "//div[@class='content-box']//h1"
    _forgot_Password_btn = "input[value='Send Me Instructions']"

    def navigateToAllCourses(self):
        self.click(self._logo, "css")
        self.click(self._all_courses, locatorType="link")

    def navigateToHome(self):
        self.click(self._logo, "css")

    def nevigateToforgetPassword(self):
        self.click(self._login_link, locatorType="link")
        self.click(self._forgot_Password, locatorType="link")
        self.waitForElement(self._forgot_Password_btn, locatorType="css")
        text = self.getText(self._page_title, locatorType="xpath")
        print(text)
        print(self.util.verifyTextContains(text,"Reset Passwordf"))


        assert self.util.verifyTextContains(text,"Reset Passwordf")


    def logOut(self):
        self.click(self._icon, locatorType="css")
        self.click(self._log_out, locatorType="css")

    def navigateToMyCourses(self):
        self.click(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.click(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                                  locatorType="xpath", pollFrequency=1)
        self.click(locator=self._user_settings_icon,
                   locatorType="xpath")
