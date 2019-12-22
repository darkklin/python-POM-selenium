import pytest
import unittest

from pages.home import forgetPassword_page
from pages.home.forgetPassword_page import ForgetPassword
from pages.home.navigation_page import NavigationPages
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.fp = ForgetPassword(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPages(self.driver)



    def test_forgetPassword(self):
        self.nav.logOut()
        self.nav.nevigateToforgetPassword()



