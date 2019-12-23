import pytest
import unittest

from pages.home import forgetPassword_page
from pages.home.forgetPassword_page import ForgetPasswordPage
from pages.home.navigation_page import NavigationPages
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ForgetPassword(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.fp = ForgetPasswordPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPages(self.driver)

    def test_forgetInvalidPassword(self):
        self.nav.logOut()
        self.nav.navigateToforgetPassword()
        self.fp.resetPassword("hdghsadhasd@sadasdsa.com")
        self.ts.markFinal("test_forgetInvalidPassword", self.fp.verifyResetPasswordFail(),
                          "invalid notification test pass")
