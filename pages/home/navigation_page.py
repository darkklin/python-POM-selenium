import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPages(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = "a[class*='logo']"
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"
    _log_out = "a[href*='out']"
    _icon = "img[class='gravatar']"

    def navigateToAllCourses(self):
        self.click(self._logo, "css")
        self.click(self._all_courses, locatorType="link")

    def navigateToHome(self):
        self.click(self._logo, "css")

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
