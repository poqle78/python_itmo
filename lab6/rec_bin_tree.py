def recursive_gen_bin_tree(root: int, height: int) -> dict:
    """
    Функция создания бинарного дерева

    :param height: Глубина дерева. Натуральное число.
    :param root: Корень дерева. Принимает только целое значение.
    :return: Возвращает дерево в виде словаря.
    """

    # Выход из рекурсии
    if height == 1:
        return {root: []}

    # Создание левого и правого потомка рекурсивным способом.
    left_leaf = recursive_gen_bin_tree(root ** 2, height - 1)
    right_leaf = recursive_gen_bin_tree(root - 2, height - 1)

    return {root: [left_leaf, right_leaf]}

