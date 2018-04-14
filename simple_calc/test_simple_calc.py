import unittest
from simple_calc import arithmetics

class test_simple_calc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(arithmetics(1, 1, "add"), 2)
        self.assertEqual(arithmetics(-1, 1, "add"), 0)
        self.assertEqual(arithmetics(-1, -1, "add"), -2)

    def test_subtract(self):
        self.assertEqual(arithmetics(1, 1, "subtract"), 0)
        self.assertEqual(arithmetics(-1, 1, "subtract"), -2)
        self.assertEqual(arithmetics(-1, -1, "subtract"), 0)

    def test_multiply(self):
        self.assertEqual(arithmetics(1, 1, "multiply"), 1)
        self.assertEqual(arithmetics(-1, 1, "multiply"), -1)
        self.assertEqual(arithmetics(-1, -1, "multiply"), 1)

    def test_divide(self):
        self.assertEqual(arithmetics(2, 1, "divide"), 2)
        self.assertEqual(arithmetics(-2, 1, "divide"), -2)
        self.assertEqual(arithmetics(-2, -1, "divide"), 2)

        with self.assertRaises(ZeroDivisionError):
            arithmetics(1, 0, "divide")

#TODO add
#TODO substract
#TODO multiply
#TODO divide
#TODO divide by 0 causes error