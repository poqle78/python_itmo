import requests
import sys
import logging
from typing import Callable
import functools


def logger(func: Callable = None, *, handle=sys.stdout) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Args:
        func: Декорируемая функция (None при использовании с аргументами)
        handle: Куда писать логи (sys.stdout или logging.Logger)
    """
    if func is None:
        return lambda func: logger(func, handle=handle)

    def LogInfo(msg: str):
        if isinstance(handle, logging.Logger):
            handle.info(msg)
        else:
            handle.write(f"INFO: {msg}\n")

    def LogError(msg: str):
        if isinstance(handle, logging.Logger):
            handle.error(msg)
        else:
            handle.write(f"ERROR: {msg}\n")

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Callable:
        LogInfo(f"Старт вызова: {func.__name__} args={args}, kwargs={kwargs}")

        try:
            result = func(*args, **kwargs)
            LogInfo(f"Успешное завершение: {func.__name__} -> {result}")
            return result

        except Exception as e:
            LogError(f"Исключение в функции: {func.__name__}: {type(e).__name__}: {e}")
            raise e

    return inner


logging.basicConfig(
    filename="currency_file.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

file_logger = logging.getLogger("currency_file")


@logger(handle=file_logger)
def get_currencies(currency_codes: list[str] = ('USD', 'EUR'),
                   url: str = 'https://www.cbr-xml-daily.ru/daily_json.js') -> dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).
        url (str): ссылка
    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Ошибка при запросе к API: {e}")

    try:
        data = response.json()
    except ValueError as e:
        raise ValueError(f"Некорректный JSON: {e}")

    currencies = {}
    if "Valute" in data:
        for code in currency_codes:
            if code in data["Valute"]:
                value = data["Valute"][code]["Value"]
                if isinstance(value, (int, float)):
                    currencies[code] = value
                else:
                    raise TypeError(f"Курс валюты {value} имеет неверный тип")
            else:
                raise KeyError(f"Не существует ключа {code}")
    else:
        raise KeyError("Валюта отсутствует в данных")
    return currencies



