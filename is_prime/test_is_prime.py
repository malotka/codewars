import unittest
from is_prime import is_prime

class test_is_prime(unittest.TestCase):
    def test_less_or_eq_one(self):
        self.assertEqual(is_prime(-1), False)
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)

    def test_two_and_three(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)

    def test_any_other_num(self):

        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(9), False)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(45), False)

    def test_any_other_input(self):
        with self.assertRaises(TypeError):
            is_prime("abc")

#for num <= 1 return false
#for num <= 3 return true
#for num > 3 check if modulo == 0
#for any other input type - TypeError