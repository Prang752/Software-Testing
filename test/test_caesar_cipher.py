import unittest
from coe_number.caesar_cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_lowercase_shift(self):
        self.assertEqual(caesarCipher("abc", 2), "cde")

    def test_uppercase_shift(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_wrap_around(self):
        self.assertEqual(caesarCipher("xyz", 3), "abc")

    def test_non_alpha_characters(self):
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_large_k(self):
        self.assertEqual(caesarCipher("abc", 28), "cde")  # k % 26 = 2

    def test_no_shift(self):
        self.assertEqual(caesarCipher("NoChange", 0), "NoChange")

    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 5), "")

if __name__ == "__main__":
    unittest.main()
