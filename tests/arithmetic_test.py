import unittest
from app.arithmetics.arithmetic import *
from app import create_app


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

    def test_arithmetic_evaluation(self):
        data = "100-50/5*2+5"

        result = arithmetic_evaluation(expression=data)

        self.assertEqual(result, 85.0, "result should be 85.0")


class TestArithmeticBlueprint(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        pass

    def test_parent_endpoint(self):
        response = self.client.get("/arithmetic/")

        expected_response = "This is the arithmetics blueprint"

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.text, expected_response, "Not the expected response")

    def test_addition_endpoint(self):
        response = self.client.post("/arithmetic/addition/", json={"data": [2, 3, 5]})

        expected_response = {"result": 10}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_subtraction_endpoint(self):
        response = self.client.post(
            "/arithmetic/subtraction/", json={"data": [20, 3, 5]}
        )

        expected_response = {"result": 12}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_multiplication_endpoint(self):
        response = self.client.post(
            "/arithmetic/multiplication/", json={"data": [2, 2, 5]}
        )

        expected_response = {"result": 20}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_division_endpoint(self):
        response = self.client.post("/arithmetic/division/", json={"data": [400, 8, 2]})

        expected_response = {"result": 25}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_root_endpoint(self):
        response = self.client.post("/arithmetic/root/", json={"data": {"number": 100}})

        expected_response = {"result": 10}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_exponent_endpoint(self):
        response = self.client.post("/arithmetic/exponent/", json={"data": [2, 2, 4]})

        expected_response = {"result": 256}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_floor_endpoint(self):
        response = self.client.post("/arithmetic/floor/", json={"data": [45, 7, 5]})

        expected_response = {"result": 1}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_modulo_endpoint(self):
        response = self.client.post("/arithmetic/modulo/", json={"data": [12, 3]})

        expected_response = {"result": 0}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")

    def test_expression_evaluation_endpoint(self):
        response = self.client.post(
            "/arithmetic/expression_eval/", json={"data": "100-50/5*2+5"}
        )

        expected_response = {"result": 85.0}

        self.assertEqual(response.status_code, 200, "Something went wrong")
        self.assertEqual(response.json, expected_response, "Not the expected response")


if __name__ == "__main__":
    unittest.main()
