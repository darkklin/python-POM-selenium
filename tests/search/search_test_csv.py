import unittest
import pytest
from pages.home.login_page import LoginPage
from pages.search.search_page import SearchPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCVSData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class SearchTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sp = SearchPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCVSData("..\\testdata.csv"))
    @unpack
    def test_pushCourse(self, courseName, ccNum, ccExp, ccCVV):
        self.sp.searchCourse(courseName)
        self.sp.fillCreditCard(ccNum, ccExp, ccCVV)
