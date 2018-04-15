import unittest
from sort_by_len import sort

class test_sort_by_len(unittest.TestCase):

    def test_sort(self):
        self.assertListEqual(sort(["beg", "life", "i", "to"]), ["i", "to", "beg", "life"])
        self.assertListEqual(sort(["a longer sentence", "the longest sentence", "a short sentence"]), ["a short sentence", "a longer sentence", "the longest sentence"])

        #type error - int has no length
        with self.assertRaises(TypeError):
            sort([1, 3212, 223, 412122])


#TODO sort words
#TODO sort sentences
#TODO what if arr contains numbers - type error