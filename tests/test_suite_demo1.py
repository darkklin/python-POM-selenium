import glob
import unittest

from tests.home.test_login import TestLogin
from tests.search.test_search import TestSearch
from tests.search.test_search_csv import TestSearchCsv

test_files = glob.glob('test_*.py')
module_strings = [test_file[0:len(test_file)-3] for test_file in test_files]
suites = [unittest.defaultTestLoader.loadTestsFromName(TestLogin) for test_file in module_strings]
suites = [unittest.defaultTestLoader.loadTestsFromName(TestSearch) for test_file in module_strings]
suites = [unittest.defaultTestLoader.loadTestsFromName(TestSearchCsv) for test_file in module_strings]

test_suite = unittest.TestSuite(suites)
test_runner = unittest.TextTestRunner().run(test_suite)
