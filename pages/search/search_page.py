from base.basepage import BasePage
import utilities.custom_logger as cl
import logging

_card_number = "//*[@id='root']/form/span[2]/span/input"
_Expiration_Date = "//*[@id='root']/form/span[2]/span/input"
_CVC_Code = "//input[@autocomplete='cc-csc']"
_Postal_Code = "//input[@autocomplete='postal-code']"
_confirm_purchase = "//label[@for='spc-primary-submit']"
_logo = "a[class*='logo']"


class SearchPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def searchCourse(self, name_course):
        self.sendKeys(name_course, "search-courses")
        self.click("search-course-buttoNn")
        self.click("//div[contains(text(),'" + name_course + "')]", locatorType="xpath")
        self.click("enroll-button-top")
        self.webScroll("down")

    def fillCreditCard(self, card_number, cvc, exp_date):
        self.frame_switch('__privateStripeFrame5')
        self.sendKeys(card_number, _card_number, "xpath")
        self.sendKeys(cvc, _CVC_Code, "xpath")
        self.frame_switch()
        self.frame_switch('__privateStripeFrame6')
        self.sendKeys(exp_date, _Expiration_Date, "xpath")
        self.frame_switch()
        self.frame_switch('__privateStripeFrame8')
        self.sendKeys("123454", _Postal_Code, "xpath")
        self.frame_switch()
        self.click("agreed_to_terms_checkbox")
        self.util.sleep(2)
        self.click(_confirm_purchase, "xpath")
