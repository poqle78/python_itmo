import logging
import math
from typing import Callable
import sys
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
    filename="quadratic.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

file_logger = logging.getLogger("quadratic")

@logger(handle=file_logger)
def solve_quadratic(a, b, c):
    """
    Функция для вычисления корней квадратного уравнения.
    :param a: коэффициент a
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни этого квадратного уравнения
    """
    logging.info(f"Solving equation: {a}x^2 + {b}x + {c} = 0")

    # Ошибка типов
    for name, value in zip(("a", "b", "c"), (a, b, c)):
        if not isinstance(value, (int, float)):
            logging.critical(f"Parameter '{name}' must be a number, got: {value}")
            raise TypeError(f"Coefficient '{name}' must be numeric")

    #Ошибка: a == 0 и b == 0
    if a == 0 and b == 0:
        logging.critical("The equation doesn't make sense")
        raise ValueError("a and b cannot be a zero")

    # Ошибка: a == 0
    if a == 0:
        logging.error("Coefficient 'a' cannot be zero")
        raise ValueError("a cannot be zero")

    d = b*b - 4*a*c
    logging.debug(f"Discriminant: {d}")

    if d < 0:
        logging.warning("Discriminant < 0: no real roots")
        return None

    if d == 0:
        x = -b / (2*a)
        logging.info("One real root")
        return (x,)

    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    logging.info("Two real roots computed")
    return root1, root2

