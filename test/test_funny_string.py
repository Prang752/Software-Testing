import unittest
from coe_number.funny_string import funnyString


class TestFunnyString(unittest.TestCase):

    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")

        self.assertEqual(funnyString("bcxz"), "Not Funny")

        self.assertEqual(funnyString("abcd"), "Not Funny")

        self.assertEqual(funnyString("madam"), "Funny")

        self.assertEqual(funnyString("racecar"), "Funny")

        self.assertEqual(funnyString("abccba"), "Funny")

        self.assertEqual(funnyString(""), "Funny")

        self.assertEqual(funnyString("a"), "Funny")

        self.assertEqual(funnyString("z"), "Funny")

        self.assertEqual(funnyString("abcdedcba"), "Funny")

        self.assertEqual(funnyString("abed"), "Not Funny")


unittest.main()
