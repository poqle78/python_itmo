import unittest
from unittest.mock import patch, Mock
import requests
from lab_7 import get_currencies, logger
import io


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def f(x):
            return x * 2

        @logger(handle=self.stream)
        def error_f(x):
            raise ValueError("error")

        self.f = f
        self.error_f = error_f

    def test_success(self):
        self.f(78)
        logs = self.stream.getvalue()
        self.assertIn('INFO: Старт вызова: ', logs)
        self.assertIn('INFO: Успешное завершение: ', logs)
        self.assertIn('156', logs)


    def test_error(self):
        with self.assertRaises(ValueError):
            self.error_f(78)

        logs = self.stream.getvalue()

        self.assertRegex(logs, "ERROR")
        self.assertRegex(logs, "ValueError")
        self.assertRegex(logs, "error")


if __name__ == '__main__':
    unittest.main()