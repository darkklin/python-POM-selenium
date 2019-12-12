import unittest
# import your test modules
from tests.home.test_login import TestLogin
from tests.search.test_search import SearchTest
from tests.search.test_search_csv import SearchTest1Two

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestLogin))
# suite.addTests(loader.loadTestsFromModule(SearchTest1Two))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)


# run the suit >>> pytest -n 2 tests\test_suite_demo.py --browser firefox
# run  parallelization
# pip install pytest-xdist  >> pytest -n NUM

