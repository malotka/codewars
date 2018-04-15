import unittest
from sum import find_sum

class test_sum_of_multiples_3_and_5(unittest.TestCase):

     def test_multiples_of_3_and_5(self):
         self.assertEqual(find_sum(5), 8)
         self.assertEqual(find_sum(10), 33)




#todo iterate in range of n and add:
#todo multiples of 3
#todo multiples of 5
#