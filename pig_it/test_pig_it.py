import unittest
from pig_it import pig_it

class TestPigIt(unittest.TestCase):
    def test_delete_first_letter(self):
        self.assertEqual(pig_it("abc"), "bc")


'''
TODO take one word and del first letter
TODO add deleted letter to an and of the word
TODO add ay to the end of the word

first letter of a word to the end
then ad ay to the word

'''