import unittest
from lab_5 import gen_bin_tree


class Tests(unittest.TestCase):
    # Проверка базового случая глубины 1
    def test_height_1(self):
        result = gen_bin_tree(5, 1)
        self.assertEqual(result, {5: []})

    # Проверка простого случая глубины 2
    def test_height_2(self):
        result = gen_bin_tree(3, 2)
        expected = {3: [{9: []}, {1: []}]}
        self.assertEqual(result, expected)

    # Проверка отрицательного корня
    def test_negative_root(self):
        result = gen_bin_tree(-4, 3)
        expected = {-4: [{16: [{256: []}, {14: []}]}, {-6: [{36: []}, {-8: []}]}]}
        self.assertEqual(result, expected)

    # Проверка нуля
    def test_zero_root(self):
        result = gen_bin_tree(0, 2)
        expected = {0: [{0: []}, {-2: []}]}
        self.assertEqual(result, expected)

    # Проверка минимального положительного значения
    def test_min_positive_value(self):
        result = gen_bin_tree(1, 2)
        expected = {1: [{1: []}, {-1: []}]}
        self.assertEqual(result, expected)

    # Проверка отрицательного значения
    def test_negative_value(self):
        result = gen_bin_tree(-1, 2)
        expected = {-1: [{1: []}, {-3: []}]}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
