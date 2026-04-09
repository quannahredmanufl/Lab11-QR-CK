import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1, 1), 2)  # positive numbers
        self.assertEqual(add(-1, -1), -2)  # negative numbers
        self.assertEqual(add(0, 5), 5)  # adding zero

    def test_subtract(self):
        self.assertEqual(subtract(5, 1), 4)  # positive numbers
        self.assertEqual(subtract(-1, -1), 0)  # negative numbers
        self.assertEqual(subtract(5, 0), 5)  # subtracting zero

    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, 15), -15)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(2, 8), 4)  # 10 / 2
        self.assertEqual(divide(10, 0), 0)  # 0 / 5
        self.assertEqual(divide(-2, 16), -8)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 10, 0)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3)  # log base 2 of 8 = 3
        self.assertEqual(logarithm(10, 100), 2)  # log base 10 of 100 = 2
        self.assertEqual(logarithm(2, 1), 0)  # log of 1 is always 0

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 0, 8)

    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(3, -15)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)

    def test_sqrt(self):  # 3 assertions
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(121), 11)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()