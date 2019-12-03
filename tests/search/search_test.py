import unittest
import pytest

from pages.home.login_page import LoginPage
from pages.search.search_page import SearchPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SearchTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.sp = SearchPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_pushCourse(self):
        self.lp.login("test@email.com", "abcabc")
        self.sp.searchCourse("JavaScript for beginners")
        self.sp.fillCreditCard("3333333222324235", "222", "0520")
