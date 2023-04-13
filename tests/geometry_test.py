import unittest
from app.geometry.geometry import *


class TestGeometryCalculations(unittest.TestCase):
    def test_rectangle_perimeter(self):
        length = 10
        width = 15

        result = rectangle_perimeter(length, width)

        self.assertEqual(result, 50, "result should be 50")

    def test_circle_perimeter(self):
        radius = 12

        result = circle_perimeter(radius)

        self.assertEqual(result, 75.39816, "result should be 75.39816")

    def test_triangle_perimeter(self):
        side_1 = 30
        side_2 = 50
        side_3 = 30

        result = triangle_perimeter(side_1, side_2, side_3)

        self.assertEqual(result, 110, "result should be 110")

    def test_rectangle_area(self):
        length = 34
        width = 43

        result = rectangle_area(length, width)

        self.assertEqual(result, 1462, "result should be 1462")

    def test_circle_area(self):
        radius = 15

        result = circle_area(radius)

        self.assertEqual(result, 706.85775, "result should be 706.85775")

    def test_triangle_area(self):
        base = 23
        height = 34

        result = triangle_area(base, height)

        self.assertEqual(result, 391, "result should be 391")

    def test_cube_volume(self):
        side = 99

        result = cube_volume(side)

        self.assertEqual(result, 970299, "result should be 970299")

    def test_cylinder_volume(self):
        radius = 21
        height = 75

        result = cylinder_volume(radius, height)

        self.assertEqual(result, 103908.08925, "result should be 103908.08925")

    def test_sphere_volume(self):
        radius = 21

        result = sphere_volume(radius)

        self.assertEqual(result, 38792.35332, "result should be 38792.35332")


if __name__ == "__main__":
    unittest.main()
