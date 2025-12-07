import unittest
from unittest.mock import patch, Mock
import requests
from lab_7 import get_currencies


class TestGetCurrencies(unittest.TestCase):

    @patch('lab_7.requests.get')
    def test_valid_currencies(self, mock_get):
        """Проверка корректного возврата реальных курсов"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.50},
                "EUR": {"Value": 85.30}
            }
        }
        mock_get.return_value = mock_response

        result = get_currencies(['USD', 'EUR'])
        expected = {'USD': 75.50, 'EUR': 85.30}
        self.assertEqual(result, expected)

    @patch('lab_7.requests.get')
    def test_nonexistent_currency(self, mock_get):
        """Проверка поведения при несуществующей валюте"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 75.50}
            }
        }
        mock_get.return_value = mock_response

        with self.assertRaises(KeyError) as context:
            get_currencies(['XYZ'])

        self.assertIn("Не существует ключа XYZ", str(context.exception))

    @patch('lab_7.requests.get')
    def test_connection_error(self, mock_get):
        """Проверка выброса ConnectionError"""
        mock_get.side_effect = requests.exceptions.ConnectionError("Сеть недоступна")

        with self.assertRaises(ConnectionError) as context:
            get_currencies()

        self.assertIn("Ошибка при запросе к API", str(context.exception))

    @patch('lab_7.requests.get')
    def test_value_error_invalid_json(self, mock_get):
        """Проверка выброса ValueError при некорректном JSON"""
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("Некорректный JSON")
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            get_currencies(['USD'])

        self.assertIn("Некорректный JSON", str(context.exception))

    @patch('lab_7.requests.get')
    def test_key_error_no_valute(self, mock_get):
        """Проверка выброса KeyError при отсутствии ключа Valute"""
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        with self.assertRaises(KeyError) as context:
            get_currencies(['USD'])

        self.assertIn("Валюта отсутствует в данных", str(context.exception))

    @patch('lab_7.requests.get')
    def test_type_error_invalid_value_type(self, mock_get):
        """Проверка TypeError при неверном типе значения курса"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": "arbuz"}
            }
        }
        mock_get.return_value = mock_response

        with self.assertRaises(TypeError) as context:
            get_currencies(['USD'])

        self.assertIn("Курс валюты arbuz имеет неверный тип", str(context.exception))


if __name__ == '__main__':
    unittest.main()