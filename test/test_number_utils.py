from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):

    def test_prime_numbers(self):
        """ทดสอบกรณีที่เป็นจำนวนเฉพาะ"""
        self.assertEqual(is_prime_list([2, 3, 5, 7, 11, 13, 17, 19]), [True, True, True, True, True, True, True, True])

    def test_non_prime_numbers(self):
        """ทดสอบกรณีที่ไม่เป็นจำนวนเฉพาะ"""
        self.assertEqual(is_prime_list([1, 4, 6, 8, 9, 10, 12, 15]), [False, False, False, False, False, False, False, False])

    def test_mixed_numbers(self):
        """ทดสอบลิสต์ที่มีทั้งจำนวนเฉพาะและไม่เป็นจำนวนเฉพาะ"""
        self.assertEqual(is_prime_list([2, 4, 5, 6, 7, 9]), [True, False, True, False, True, False])

    def test_negative_numbers(self):
        """ทดสอบกรณีที่เป็นเลขติดลบ"""
        self.assertEqual(is_prime_list([-1, -2, -3, -10]), [False, False, False, False])

    def test_large_prime_number(self):
        """ทดสอบจำนวนเฉพาะขนาดใหญ่"""
        self.assertEqual(is_prime_list([101, 103, 107, 109]), [True, True, True, True])

    def test_large_non_prime_number(self):
        """ทดสอบจำนวนที่ไม่เป็นจำนวนเฉพาะขนาดใหญ่"""
        self.assertEqual(is_prime_list([100, 102, 104, 110]), [False, False, False, False])

    def test_empty_list(self):
        """ทดสอบกรณีที่เป็นลิสต์ว่าง"""
        self.assertEqual(is_prime_list([]), [])

    def test_single_prime_number(self):
        """ทดสอบกรณีที่มีเลขเดียวและเป็นจำนวนเฉพาะ"""
        self.assertEqual(is_prime_list([7]), [True])

    def test_single_non_prime_number(self):
        """ทดสอบกรณีที่มีเลขเดียวและไม่เป็นจำนวนเฉพาะ"""
        self.assertEqual(is_prime_list([1]), [False])

if __name__ == "__main__":
    unittest.main()
