from unittest import TestLoader, TextTestRunner


def run_tests():
    loader = TestLoader()
    suite = loader.discover("tests", pattern="*_test.py")
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
