def gen_bin_tree(root: int, height: int, left_leaf=lambda root: root ** 2, right_leaf=lambda root: root - 2) -> dict:
    """
    Функция создания бинарного дерева нерекурсивным способом.

    :param height: глубина дерева
    :param root: корень дерева
    :param left_leaf: лямбда-функция по созданию левого потомка
    :param right_leaf: лямбда-функция по созданию правого потомка
    :return: возвращает бинарное дерево словарем
    """
    tree = {}  # словарь, в котором будет хранится бинарное дерево
    depth = 1  # текущая глубина
    flag = [(root, tree,
             depth)]  # массив, состоящий из кортежей, которые в свою очередь содержат текущее значение в ячейке, дерево, текущую глубину
    while flag:

        cur_val, bond, cur_depth = flag.pop(0)
        bond[cur_val] = []  # вносим в переменную bond текущее значение ячейки

        # вносим в массив flag только те ячейки, которые не превышают глубину
        if cur_depth + 1 <= height:
            # добавляем в дерево левого и правого потомков
            l_l, r_l = {}, {}
            bond[cur_val].append(l_l)
            bond[cur_val].append(r_l)
            flag.append((left_leaf(cur_val), l_l, cur_depth + 1))
            flag.append((right_leaf(cur_val), r_l, cur_depth + 1))

    # возвращаем итоговое дерево
    return tree



