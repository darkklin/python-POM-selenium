import unittest

import pytest

from pages.home.navigation_page import NavigationPages
from pages.search.search_page import SearchPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class TestSearch(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SearchPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPages(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "3333333222324235", "222", "0520"),
          ("Selenium WebDriver With Java", "3333333222324235", "222", "0526"))
    @unpack
    def test_pushCourse(self, courseName, ccNum, ccExp, ccCVV):
        self.sp.searchCourse(courseName)
        self.sp.fillCreditCard(ccNum, ccExp, ccCVV)
