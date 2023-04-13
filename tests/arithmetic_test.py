import unittest
from app.arithmetics.arithmetic import *


class TestArithmeticCalculations(unittest.TestCase):
    def test_arithmetic_sum(self):
        data = (2, 3, 5)

        result = arithmetic_sum(*data)

        self.assertEqual(result, 10, "result should be 10")

    def test_arithmetic_difference(self):
        data = (10, 3, 2)

        result = arithmetic_difference(*data)

        self.assertEqual(result, 5, "result should be 5")

    def test_arithmetic_multiplication(self):
        data = (6, 4, 5)

        result = arithmetic_multiplication(*data)

        self.assertEqual(result, 120, "result should be 120")

    def test_arithmetic_division(self):
        data = (100, 4, 5)

        result = arithmetic_division(*data)

        self.assertEqual(result, 5, "result should be 5")

    def test_arithmetic_exponent(self):
        data = (2, 3, 4)

        result = arithmetic_exponent(*data)

        self.assertEqual(result, 4096, "result should be 4096")

    def test_arithmetic_root(self):
        number = 100

        result = arithmetic_root(number)

        self.assertEqual(result, 10, "result should be 10")

    def test_arithmetic_floor(self):
        data = (45, 7, 5)

        result = arithmetic_floor(*data)

        self.assertEqual(result, 1, "result should be 1")

    def test_arithmetic_modulo(self):
        data = (45, 7)

        result = arithmetic_modulo(*data)

        self.assertEqual(result, 3, "result should be 3")


if __name__ == "__main__":
    unittest.main()
