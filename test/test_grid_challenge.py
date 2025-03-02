import unittest
from coe_number.grid_challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_valid_grid(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_unsortable_grid(self):
        grid = ["ebacd", "aghij", "olmkn", "trpqs", "xywuv"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_single_row(self):
        grid = ["zyxwv"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_single_column(self):
        grid = ["a", "b", "c", "d"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_unsorted_single_column(self):
        grid = ["d", "c", "b", "a"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_large_grid(self):
        grid = ["abcdefghijklmnopqrstuvwxyz" for _ in range(1000)]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_minimal_input(self):
        grid = ["a"]
        self.assertEqual(gridChallenge(grid), "YES")

unittest.main()
