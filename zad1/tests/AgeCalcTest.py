from sample.AgeCalc import *
import unittest
from hamcrest import *

class AgeCalcTest(unittest.TestCase):

    def setUp(self):
        self.temp = AgeCalc

    def testEquals(self):
        assert_that(self.temp.age("Ziemia", 1000000000), equal_to(31.69))

    def testAnyOf(self):
        assert_that(self.temp.age("Merkury", 1000000000), equal_to(131.57))

    def test_age_Mercury2(self):
        assert_that(self.temp.age("Merkury", 1000000000), close_to(130, 2))

    def test_age_Venus(self):
        assert_that(self.temp.age("Wenus", 1000000000), equal_to(51.51))

    def test_age_Venus2(self):
        assert_that(self.temp.age("Wenus", 1000000000), greater_than(50))

    def test_age_Mars(self):
        assert_that(self.temp.age("Mars", 1000000000), equal_to(16.85))

    def test_age_Mars2(self):
        assert_that(self.temp.age("Mars", 1000000000), less_than(20))

    def test_age_Jupiter(self):
        assert_that(self.temp.age("Jowisz", 1000000000), equal_to(2.67))

    def test_age_Saturn(self):
        assert_that(self.temp.age("Saturn", 1000000000), equal_to(1.08))

    def test_age_Uranus(self):
        assert_that(self.temp.age("Uran", 1000000000), equal_to(0.38))

    def test_age_Neptune(self):
        assert_that(self.temp.age("Neptun", 1000000000), equal_to(0.19))

    def test_age_Float(self):
        assert_that(self.temp.age("Neptun", 1000000000.2), equal_to(0.19))

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
