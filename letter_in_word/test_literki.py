import unittest
from literki import contains

class literki(unittest.TestCase):

    def test_contains_letter(self):
        self.assertEqual(True, contains("word", "w"))
        self.assertEqual(True, contains("Word", "W"))
        self.assertEqual(False, contains("word", "z"))

    def test_contains_uppercse(self):
        self.assertEqual(True, contains("word", "W"))

    def test_contains_other_types(self):
        with self.assertRaises(ValueError):
            contains("word", 1)

        with self.assertRaises(ValueError):
            contains("word", 1.5)

        with self.assertRaises(ValueError):
            contains("word", False)

    def test_contains_more_letters(self):
        with self.assertRaises(ValueError):
            contains("word", "afds")
