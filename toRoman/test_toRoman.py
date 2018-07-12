from toRoman import to_roman
from toNumeral import to_numeral
import unittest

class toRoman(unittest.TestCase):

    def test_returns_Is_for_less_equals_3(self):
        self.assertEqual('I', to_roman(1))
        self.assertEqual("II", to_roman(2))
        self.assertEqual("III", to_roman(3))

    def test_returns_IV_for_4(self):
        self.assertEqual("IV", to_roman(4))

    def test_returns_V_for_5(self):
        self.assertEqual('V', to_roman(5))

    def test_returns_VI_for_6(self):
        self.assertEqual("VI", to_roman(6))
        self.assertEqual("VII", to_roman(7))
        self.assertEqual("VIII", to_roman(8))

    def test_returns_IX_for_9(self):
        self.assertEqual('IX', to_roman(9))

    def test_returns_X_for_10(self):
        self.assertEqual('X', to_roman(10))

    def test_returns_XI_for_11(self):
        self.assertEqual('XI', to_roman(11))

    def test_returns_XL_for_40(self):
        self.assertEqual('XL', to_roman(40))

    def test_returns_MMMCMXCIX_for_3999(self):
        self.assertEqual('MMMCMXCIX', to_roman(3999))

    def test_returns_error_for_non_ints(self):
        self.assertEqual('Error', to_roman('halp'))

    def test_returns_error_for_less_than_1(self):
        self.assertEqual('Less than 1!', to_roman(0))

    def test_returns_error_for_more_than_3999(self):
        self.assertEqual('More than 3999!', to_roman(4000))
""""
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

toRoman should return the Roman numeral representation for all integers 1 to 3999.
toRoman should fail when given an integer outside the range 1 to 3999.
toRoman should fail when given a non-integer number.
fromRoman should take a valid Roman numeral and return the number that it represents.
fromRoman should fail when given an invalid Roman numeral.
If you take a number, convert it to Roman numerals, then convert that back to a number, you should end up with the number you started with. So fromRoman(toRoman(n)) == n for all n in 1..3999.
toRoman should always return a Roman numeral using uppercase letters.
fromRoman should only accept uppercase Roman numerals (i.e. it should fail when given lowercase input).
"""