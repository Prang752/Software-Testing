
import unittest
from coe_number.alternating_characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating_characters(self):

        self.assertEqual(alternatingCharacters("ABABAB"), 0)

        self.assertEqual(alternatingCharacters("AABBAA"), 4)

        self.assertEqual(alternatingCharacters("AAAA"), 3)

        self.assertEqual(alternatingCharacters("A"), 0)

        self.assertEqual(alternatingCharacters(""), 0)

        self.assertEqual(alternatingCharacters("AB"), 0)

        self.assertEqual(alternatingCharacters("AABBAAAB"), 4)

        self.assertEqual(alternatingCharacters("ABABABAB"), 0)


unittest.main()
