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
    def test_search(self):
        self.lp.login("test@email.com", "abcabc")
        self.sp.searchCourse()