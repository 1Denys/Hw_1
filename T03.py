import unittest
from unittest.case import skip


"""
 * Вам дано масив цілих чисел nums.
 * Поверніть мінімальну кількість операцій необхідних для того, щоб зробити nums
 * строго зростаючим.
 *
 * Одна операція – це збільшення будь-якого елемента в масиві на 1.
 *
 * Масив nums буде строго зростаючим якщо
 * nums[i] < nums[i+1] для всіх 0 <= i < nums.length - 1
 * Масив з одним елементом вважається строго зростаючим.
 *
 * Приклад:
 * Input: nums = [1,1,1]
 * Output: 3
 *
 * Пояснення: строго зростаючим буде масив [1,2,3], тому необхідно збільшити
 * nums[1] рівно 1 раз, а nums[2] 2 разу.
"""


def solve(nums):
    # Write your solution here
    n = []
    m = sorted(nums)[len(nums) // 2]
    for i2 in nums:
        n.append(abs(i2 - m))
    summ = sum(n)
    return summ

a = solve([1,1,1])
print(a)

@skip  # remove this to run tests
class T03(unittest.TestCase):
    testCases = [
        {"input": [[1, 1, 1]], "expected": 3},
        {"input": [[1, 2, 1]], "expected": 2},
        {"input": [[-3]], "expected": 0},
        {"input": [[-3, -2, 10]], "expected": 0},
        {"input": [[-3, -2, -5]], "expected": 4},
        {"input": [[1, 5, 90, 0]], "expected": 91},
        {"input": [[1, 0, 5, 4, 90, 0]], "expected": 95},
    ]

    def test(self):
        print("Executing: 03 Min number of changes to make array increasing")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(test["input"][0]), test["expected"])
