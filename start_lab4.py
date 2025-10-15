from timeit import *
import matplotlib.pyplot as plt


# Рекурсивная функция для вычисления факториала
def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n - 1)


# Функция для вычисления факториала через цикл
def fact_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Создаем список значений n для которых будем измерять время
n_values = [n for n in range(5, 101, 5)]

# Массивы для хранения результатов замеров времени
recursive_times = []
iterative_times = []

for n in n_values:
    # Измеряем время работы рекурсивной функции
    recursive_time = timeit(lambda: fact_recursive(n), number=1000)
    recursive_times.append(recursive_time)

    # Измеряем время работы итерационной функции
    iterative_time = timeit(lambda: fact_iterative(n), number=1000)
    iterative_times.append(iterative_time)

# Построение графика
plt.plot(n_values, recursive_times, label='Рекурсия')
plt.plot(n_values, iterative_times, label='Цикл')
plt.xlabel('Значение N')
plt.ylabel('Время выполнения')
plt.title('Сравнение времени выполнения рекурсии и цикла для вычисления факториала')
plt.legend()
plt.grid(True)
plt.show()
