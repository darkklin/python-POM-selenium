from pages.home.login_page import LoginPage
from pages.home.navigation_page import NavigationPages
from utilities.teststatus import TestStatus
from utilities.util import Util
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPages(self.driver)


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.nav.logOut()
        self.lp.login("dasdasd@asdasd.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        print("start"*20)
        self.nav.navigateToHome()
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")




