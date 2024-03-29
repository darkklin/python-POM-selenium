import contextlib

import allure
from selenium.webdriver.common.by import By
from traceback import print_stack

from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from allure_commons.types import AttachmentType

import logging
import time
import os


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
            # return destination file to be able to attach the screen shot to allure report
            return destinationFile
        except:
            self.log.error("### Exception Occurred when taking screenshot")
    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def cleanField(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.clear()
            self.log.info("Clear the text from field with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear the text from  locator: " + locator +
                          " locatorType: " + locatorType)

    def getElementList(self, locator, locatorType="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def click(self, locator="", locatorType="id", element=None):
        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            allure.attach.file(self.screenShot("Click-Fail"), name="Screenshot click fail", attachment_type=AttachmentType.PNG)
            assert False, "Fail to click on:" + locator + " locatorType: " + locatorType

    def frame_switch(self, name_frame=""):
        """
        switch into frame with unic  frame name
        or switch back to the default (don't provide name )
        can be modify to work with not only name if need to ...
        """

        try:
            if name_frame:  # This means if locator/name is not empty
                self.driver.switch_to.frame(name_frame)
                self.log.info("switch into frame with name: " + name_frame)
            else:
                self.driver.switch_to.default_content()
                self.log.info("switch Back to default frame")
        except:
            self.log.error("Cannot switch into frame name: " + name_frame)
            assert False, "no such frame: Unable to locate frame with name :" + name_frame

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locatorType)
            allure.attach.file(self.screenShot("sendKeys"), name="Screenshot sendKeys fail", attachment_type=AttachmentType.PNG)
            assert False, "no such element: Unable to locate element:" + locator + " locatorType: " + locatorType

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            allure.attach.file(self.screenShot("getText"), name="Screenshot getText fail", attachment_type=AttachmentType.PNG)
            assert False, "no such element: Unable to locate element:" + locator + " locatorType: " + locatorType
        return text



    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present D
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not present with locator: " + locator +
                               " locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found")
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.error("Element not displayed with locator: " + locator +
                               " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.error("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        """
        Check if element is present
        """
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.error("Element not present with locator: " + locator +
                               " locatorType: " + str(byType))
                return False
        except:
            self.log.error("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            allure.attach.file(self.screenShot("waitForElement"), name="Screenshot waitForElement fail", attachment_type=AttachmentType.PNG)
            assert False, "no such element: Unable to locate element:" + locator + " locatorType: " + locatorType

        return element

    def webScroll(self, direction="up"):
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def page_has_loaded(self):
        self.log.info("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def wait_loading(self):
        wait_time = 0
        while self.driver.execute_script('return document.readyState;') != 'complete' and wait_time < 10:
            # Scroll down to bottom to load contents, unnecessary for everyone
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            wait_time += 0.1
            time.sleep(0.1)
        print('Load Complete.')


