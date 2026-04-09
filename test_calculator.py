import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        if (add(1, 1) == 2):
            return true

    def test_subtract(self):
        if (subtract(5, 1) == 4):
            return true

    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, 15), -15)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(2, 8), 4)  # 10 / 2
        self.assertEqual(divide(10, 0), 0)  # 0 / 5
        self.assertEqual(divide(-2, 16), -8)

   def test_divide_by_zero(self): # 1 assertion
       if a == 0:
           divide(a,b)
           return true

    def test_logarithm(self):
        if (logarithm(2,8)==3):
            return true

    def test_log_invalid_base(self): # 1 assertion
        if b == 0:
            logarithm(a,b)
            return true

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

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