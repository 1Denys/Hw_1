import unittest
from unittest.case import skip


"""
 * Даний масив чисел nums.
 * Running sum для елемента 'i' заданий як сума елементів [0..i], тобто
 * runningSum[i] = nums[0] + nums[1] + .. + nums[i]
 * Обчисліть та поверніть масив running sum.
 *  
 * Додаткові умови:
 * 1. Не змінюйте вхідний масив
 * 2. Старайтеся використати O(1) додаткової пам'яті (без урахування вихідного масиву)
 * 
 * Приклад:
 * Input: nums = [1, 2, 3]
 * Output: [1, 3, 6], бо [1, 1+2, 1+2+3]
"""

def solve(nums):
    # Write your solution here
    summ = []
    for i in range(1, len(nums) + 1):
        summ.append(sum(nums[: i]))
    return summ

#a = solve([1, 2, 3])
#print(a)

#@skip  # remove this to run tests
class T01(unittest.TestCase):
    testCases = [
        {"input": [[1, 2, 3, 4, 5]], "expected": [1, 3, 6, 10, 15]},
        {"input": [[1, 2, 3, 4, 6]], "expected": [1, 3, 6, 10, 16]},
        {"input": [[1, 1, 1, 1]], "expected": [1, 2, 3, 4]},
        {"input": [[1, 2, -3, 4, 6]], "expected": [1, 3, 0, 4, 10]},
        {"input": [[-1, -1, -2, 4, 0]], "expected": [-1, -2, -4, 0, 0]}
    ]

    def test(self):
        print("Executing: 01 Running sum")

        for i, test in enumerate(self.testCases):
            with self.subTest(f"Test index: {i}"):
                self.assertEqual(solve(
                    test["input"][0]), test["expected"])
