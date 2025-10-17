from lab_5 import gen_bin_tree


# Запуск функции с вводом данных с клавиатуры
start = input("Хотите построить бинарное дерево? (да/нет) \n(В отрицательном случае будет базовый тест height = 6, root = 5): ")
try:
    if start.lower() == 'да':
        try:
            height = int(input("Введите глубину дерева (любое натуральное число): "))
            root = int(input("Введите корень дерева (любое целое число): "))
            if height < 1:
                print("Требуется ввести натуральное число!")
            else:
                print(gen_bin_tree(root, height))

        except ValueError:
            print("Неверный формат данных!")
    elif start.lower() == 'нет':
        print(gen_bin_tree(5, 6))
    else:
        print('Нужно ввести "да" или "нет"!')

except Exception:
    print('Нужно ввести "да" или "нет"!')
