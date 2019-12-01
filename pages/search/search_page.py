from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

_card_number = "//*[@id='root']/form/span[2]/span/input"
_Expiration_Date = "//input[@autocomplete='cc-exp']"
_CVC_Code = "//input[@autocomplete='cc-csc']"
_Postal_Code = "//input[@autocomplete='postal-code']"


class SearchPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    def searchCourse(self):
        self.sendKeys("JavaScript", "search-courses")
        self.elementClick("search-course-button")
        self.elementClick("//div[contains(text(),'JavaScript for beginners')]", locatorType="xpath")
        self.elementClick("enroll-button-top")
        self.webScroll("down")
        self.fillCreditCard()

    def fillCreditCard(self):
        self.frame_switch()
        self.sendKeys("3333333222324235",_card_number,locatorType="xpath")
        # self.sendKeys("0520",_Expiration_Date,locatorType="xpath")
        # self.sendKeys("222",_CVC_Code,locatorType="xpath")
        # self.sendKeys("123454",_Postal_Code,locatorType="xpath")
        # self.elementClick("agreed_to_terms_checkbox")

        self.elementClick("//label[@for='spc-primary-submit']",locatorType="xpath")






