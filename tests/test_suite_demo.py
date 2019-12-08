import unittest
from tests.search.search_test import SearchTest
from tests.home.login_tests import LoginTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SearchTest)

smokeTest = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)


