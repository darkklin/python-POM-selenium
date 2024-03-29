import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPages


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPages(driver)


    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.click(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.click(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.cleanField(self._email_field)
        self.enterEmail(email)
        self.cleanField(self._password_field)
        self.enterPassword(password)
        self.clickLoginButton()



    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//*[@id='navbar']//img[@alt='test@email.com']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("Let's Kode It")



