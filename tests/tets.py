import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class TestDz(unittest.TestCase):
    def test_year_is_leap(self):
        self.assertEqual(is_year_leap(800),True)
        self.assertEqual(is_year_leap(810), False)
        self.assertEqual(is_year_leap(100), False)
        self.assertEqual(is_year_leap(16), True)
        self.assertEqual(triangle(2,3,4), True)
        self.assertEqual(triangle(2, 10, 4), False)

    def test_triangle(self):
        self.assertEqual(triangle(2, 3, 4), True)
        self.assertEqual(triangle(2, 10, 4), False)

    def test_triangle_value(self):
        self.assertEqual(triangle_value(3, 3, 3), 'Isosceles triangle ')
        self.assertEqual(triangle_value(2, 10, 4), 'Not a triangle')
        self.assertEqual(triangle_value(3, 3, 4), 'Equilateral triangle ')
        self.assertEqual(triangle_value(2, 3, 4), 'Versatile triangle')


if __name__ == '__main__':
    unittest.main()