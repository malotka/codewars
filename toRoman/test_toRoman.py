from toRoman import toRoman
import unittest

class toRoman(unittest.TestCase):

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