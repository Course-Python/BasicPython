import unittest

from main import args_sum


class TestArgsSumUnittests(unittest.TestCase):
    def test_1_2_3(self):
        self.assertEqual(args_sum(1, 2, 3), 6)
 
    def test_1(self):
        self.assertEqual(args_sum(1), 1)

    def test_true(self):
        self.assertTrue(args_sum(10, 20) < 50)

if __name__ == '__main__':
    unittest.main()
