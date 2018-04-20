import unittest
from fizz_buzz import fizz_buzz

class test_fizz_buzz(unittest.TestCase):
    def test_return_num(self):
        self.assertEqual(fizz_buzz(1), 1)
        self.assertEqual(fizz_buzz(2), 2)
        self.assertEqual(fizz_buzz(4), 4)

    def test_fizz_when_divisible_by_3(self):
        self.assertEqual(fizz_buzz(3), "fizz")
        self.assertEqual(fizz_buzz(9), "fizz")

    def test_buzz_when_divisible_by_5(self):
        self.assertEqual(fizz_buzz(5), "buzz")
        self.assertEqual(fizz_buzz(10), "buzz")

    def test_fizzbuzz_when_divisible_by_3_and_5(self):
        self.assertEqual(fizz_buzz(15), "fizzbuzz")
        self.assertEqual(fizz_buzz(30), "fizzbuzz")

    def test_string_inserted(self):
        self.assertEqual(fizz_buzz("abc"), 0)


if __name__ == '__main__':

    unittest.main()

# TODO when 1, 2, 4,... - return number
# TODO when 3 - fizz
# TODO when 5 - buzz
# TODO when divided by 3 - fizz
# TODO when divided by 5 - buzz
# TODO when divided by 3 AND 5 - fizz buzz
# TODO what if not a number?