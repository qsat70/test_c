#################################################################################
import os, pytest
import sys
import unittest
from retry import retry

# TestsuiteTestClass class provides automation test for certain features.
class TestSuiteTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Description for test class setUp function """
        print("Test Class teardown.")  

    @classmethod
    def tearDownClass(cls):
        """ Description for test class setUp function """
        print("Test Class teardown.")


    def setUp(self):
        """ Description for test case setUp function """
        print("Test Case setup.", "red") 

    def tearDown(self):
        """ Description for test case tearDown function """
        print("Test Case teardown.") 

    # ===================== Test Cases ========================

    def test_1(self):
        print("Pass Test Case")

    def test_2(self):
        """ NOTE - Fake Test Failure """
        print("Fail Test Case")
        self.fail("Fake failure")

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_3(self):
        print("Skip Test Case")
        self.skipTest("Skip this windows case")

    @pytest.mark.slow 
    def test_4(self):
        print("Fail (Assert) Test Case")
        self.assertEqual("Value_a", "Value_b")

    @retry(tries=2, delay=1)
    def test_5(self):
        print("Retry cases")
        pytest.fail("fail on pytest fail function")

@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
               

if __name__ == '__main__':
    unittest.main()
