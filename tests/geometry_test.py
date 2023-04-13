import unittest
from app.geometry.geometry import *
from app import create_app


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

    def test_sphere_area(self):
        radius = 17

        result = sphere_area(radius)

        self.assertEqual(result, 3631.67804, "result should be 3631.67804")

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


class TestGeometryBlueprint(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        pass

    def test_parent_endpoint(self):
        response = self.client.get("/geometry/")

        expected_response = "This is the geometry blueprint"

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.text, expected_response, "Not the expected response")

    def test_rectangle_perimeter_endpoint(self):
        response = self.client.post(
            "/geometry/rectangle_perimeter/", json={"data": {"length": 30, "width": 65}}
        )

        expected_response = {"result": 190}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_circle_perimeter_endpoint(self):
        response = self.client.post(
            "/geometry/circle_perimeter/", json={"data": {"radius": 25}}
        )

        expected_response = {"result": 157.0795}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_triangle_perimeter_endpoint(self):
        response = self.client.post(
            "/geometry/triangle_perimeter/",
            json={"data": {"side_1": 20, "side_2": 20, "side_3": 30}},
        )

        expected_response = {"result": 70}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_rectangle_area_endpoint(self):
        response = self.client.post(
            "/geometry/rectangle_area/", json={"data": {"length": 55, "width": 105}}
        )

        expected_response = {"result": 5775}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_circle_area_endpoint(self):
        response = self.client.post(
            "/geometry/circle_area/", json={"data": {"radius": 29}}
        )

        expected_response = {"result": 2642.07719}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_triangle_area_endpoint(self):
        response = self.client.post(
            "/geometry/triangle_area/", json={"data": {"base": 45, "height": 60}}
        )

        expected_response = {"result": 1350.0}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_sphere_area_endpoint(self):
        response = self.client.post(
            "/geometry/sphere_area/", json={"data": {"radius": 43}}
        )

        expected_response = {"result": 23235.19964}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_cube_volume_endpoint(self):
        response = self.client.post(
            "/geometry/cube_volume/", json={"data": {"side": 45}}
        )

        expected_response = {"result": 91125}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_cylinder_volume_endpoint(self):
        response = self.client.post(
            "/geometry/cylinder_volume/", json={"data": {"radius": 34, "height": 65}}
        )

        expected_response = {"result": 236059.0726}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_sphere_volume_endpoint(self):
        response = self.client.post(
            "/geometry/sphere_volume/", json={"data": {"radius": 45}}
        )

        expected_response = {"result": 381703.185}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")


if __name__ == "__main__":
    unittest.main()
