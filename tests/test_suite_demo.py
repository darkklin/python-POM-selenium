import unittest
# import your test modules
from tests.home.login_tests import LoginTests
from tests.search.search_test import SearchTest
from tests.search.search_test_csv import SearchTest1Two

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(LoginTests))
suite.addTests(loader.loadTestsFromModule(SearchTest1Two))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

# run the suit >>> pytest -n 2 tests\test_suite_demo.py --browser firefox
# run  parallelization
# pip install pytest-xdist  >> pytest -n NUM
