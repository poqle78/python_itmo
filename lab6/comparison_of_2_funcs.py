import timeit
import matplotlib.pyplot as plt
from rec_bin_tree import recursive_gen_bin_tree
from bin_tree import gen_bin_tree


try:
    flag = 1
    user_response = input(
        'Хотите ввести данные для построения графиков (да/нет)?\nЕсли нет, то будет базовый тест root = 5, height = [1, 2, 3, 4, 5, 6]: ')
    if user_response == 'да':
        root = int(input("Введите значение в корне дерева (любое целое число): "))
        print("Выберите диапозон высот бинарного дерева (2 натуральных числа)")
        h1 = int(input("Введите от: "))
        h2 = int(input("Введите до: "))
        if h1 <= 0 or h2 <= 0:
            print("Неверное введены данные!")
            flag = 0
        else:
            heights = [i for i in range(h1, h2+1)]
    elif user_response == 'нет':
        root = 5
        heights = [i for i in range(1, 7)]
    else:
        print("Неверно введены данные!")
        flag = 0

    if flag:
        iterative_times = []
        recursive_times = []

        for h in heights:
            iterative_time = timeit.timeit(lambda: gen_bin_tree(root, h), number=1000)
            recursive_time = timeit.timeit(lambda: recursive_gen_bin_tree(root, h), number=1000)

            iterative_times.append(iterative_time / 1000)
            recursive_times.append(recursive_time / 1000)

        plt.figure(figsize=(10, 6))
        plt.plot(heights, iterative_times, label='Нерекурсивный метод')
        plt.plot(heights, recursive_times, label='Рекурсивный метод')

        plt.xlabel('Высота дерева')
        plt.ylabel('Время выполнения')
        plt.title('Сравнение времени работы двух реализаций функции построения бинарного дерева')
        plt.legend()
        plt.grid(True)
        plt.show()
except ValueError:
    print("Неверно введены данные!")


