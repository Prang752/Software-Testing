import unittest
from coe_number.alternate import alternate

class TestAlternateFunction(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_all_same_character(self):
        self.assertEqual(alternate("aaaaaa"), 0)

    def test_already_alternating(self):
        self.assertEqual(alternate("abababab"), 8)

    def test_no_valid_alternating_string(self):
        self.assertEqual(alternate("abc"), 2)

    def test_large_input(self):
        s = "a" * 5000 + "b" * 5000
        self.assertEqual(alternate(s), 0)

    def test_one_character(self):
        self.assertEqual(alternate("a"), 0)

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)

unittest.main()
