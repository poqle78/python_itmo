def f(trg, nums):
    checked = []
    result = []
    flag1 = 1
    flag2 = 1
    if len(nums) > 1:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i not in checked and j not in checked:
                    if nums[i] + nums[j] == trg:
                        if flag1:
                            result.append(i)
                            result.append(j)
                            checked.append(i)
                            checked.append(j)
                            flag1 = 0
                            flag2 = 0
                        else:
                            print(f'({i}, {j})', end=' ')
                            checked.append(i)
                            checked.append(j)
        if flag2:
            print('None')
    else:
        print('The list must contain more than 1 element!')
    return result

try:
    nums = [int(i) for i in input('Введите список (через пробел): ').split()]
    trg = int(input("Введите искомую сумму: "))
    print(f(trg, nums))
except ValueError:
    print('That was no valid number')
















import unittest


# Тесты
class TestMath(unittest.TestCase):
    def test1(self):
        self.assertEqual(f(9, [2, 7, 11, 15]), [0, 1])

    def test2(self):
        self.assertEqual(f(6, [3, 2, 4]), [1, 2])

    def test3(self):
        self.assertEqual(f(6, [3, 3]), [0, 1])


if __name__ == '__main__':
    unittest.main()