import unittest
from math_operations import MathOperations

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MathOperations.add(2, 3), 5)
        self.assertEqual(MathOperations.add(-1, 1), 0)
        self.assertEqual(MathOperations.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(MathOperations.subtract(5, 3), 2)
        self.assertEqual(MathOperations.subtract(0, 5), -5)
        self.assertEqual(MathOperations.subtract(-3, -2), -1)

    def test_multiply(self):
        self.assertEqual(MathOperations.multiply(2, 3), 6)
        self.assertEqual(MathOperations.multiply(-1, 3), -3)
        self.assertEqual(MathOperations.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(MathOperations.divide(6, 3), 2)
        self.assertEqual(MathOperations.divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            MathOperations.divide(5, 0)

    def test_average(self):
        self.assertEqual(MathOperations.average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(MathOperations.average([10, 20, 30]), 20)
        with self.assertRaises(ValueError):
            MathOperations.average([])

    def test_percentage(self):
        self.assertEqual(MathOperations.percentage(50, 200), 25)
        self.assertEqual(MathOperations.percentage(1, 4), 25)
        with self.assertRaises(ValueError):
            MathOperations.percentage(5, 0)

if __name__ == "__main__":
    unittest.main()