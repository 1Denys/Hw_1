import sys
import unittest
from unittest.case import skip


"""
 * Вам дана матриця MxN цілих чисел - accounts. Де accounts[i][j] зберігає
 * кількість грошей які ith клієнт має на jth рахунку.
 * Поверніть стан найбагатшого клієнта.
 *
 * Стан клієнта це сума всіх його коштів на всіх рахунках.
 *
 * Приклад:
 * Input: accounts = [[1,5],[7,3],[3,5]]
 * Output: 10
"""


def solve(accounts):
    # Write your solution here
    summ = []
    for i in range(len(accounts)):
         summ.append(sum(accounts[i]))
    maxx = max(summ)
    return maxx

#a = solve([[1,5],[7,3],[3,5]])
#print(a)

#@skip  # remove this to run tests
class T02(unittest.TestCase):
    testCases = [
        {"input": [[[1, 2, 3], [3, 2, 1]]], "expected": 6},
        {"input": [[[1, 5], [7, 3], [3, 5]]], "expected": 10},
        {"input": [[[2, 8, 7], [7, 1, 3], [1, 9, 5]]], "expected": 17},
        {"input": [[[2, 6, 7], [7, 1, 3], [1, 9, 5]]], "expected": 15},
        {"input": [[[8], [1, 2, 3], [10, -1]]], "expected": 9}
    ]

    def test(self):
        print("Executing: 02 Richest customer")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])
