"""
https://leetcode.com/problems/adding-two-negabinary-numbers/

Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.



Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
Example 2:

Input: arr1 = [0], arr2 = [0]
Output: [0]
Example 3:

Input: arr1 = [0], arr2 = [1]
Output: [1]


Constraints:

1 <= arr1.length, arr2.length <= 1000
arr1[i] and arr2[i] are 0 or 1
arr1 and arr2 have no leading zeros


We can try to determine the last digit of the answer, then divide everything by 2 and repeat.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         result = []
#         i1, i2 = len(arr1)-1, len(arr2)-1
#         carry = 0
#         sign = 1
#         while i1 >= 0 or i2 >= 0 or carry:
#             d1 = arr1[i1] if i1 >= 0 else 0
#             d2 = arr2[i2] if i2 >= 0 else 0
#             res = d1+d2+sign*carry
#             result.append(res % 2)
#             carry = -res // 2
#
#             sign = -sign
#             i1 -= 1
#             i2 -= 1
#         return result[::-1]


# Runtime: 97 ms, faster than 35.94% of Python3 online submissions for Adding Two Negabinary Numbers.
# Memory Usage: 14.1 MB, less than 52.34% of Python3 online submissions for Adding Two Negabinary Numbers.
# https://leetcode.com/problems/adding-two-negabinary-numbers/discuss/1947103/Python-100-fastest-with-comments
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n1, n2 = len(arr1), len(arr2)
        cp, cn = 0, 0
        arr1, arr2 = arr1[::-1], arr2[::-1]
        i, result = 0, []
        while i < max(n1, n2) or cn or cp:
            d1 = arr1[i] if i < n1 else 0
            d2 = arr2[i] if i < n2 else 0
            if i % 2 == 0:
                res = cp + d1 + d2
                if res in [0, 1]:
                    result.append(res)
                    cp = 0
                elif res > 1:
                    result.append(res % 2)
                    cp, cn = 1, 1
                else:
                    result.append(-res)
                    cp, cn = 0, 1
            else:
                res = cn + d1 + d2
                if res in [0, 1]:
                    result.append(res)
                    cn = 0
                else:
                    result.append(res % 2)
                    cp -= 1
                    cn = 0
            i += 1

        while len(result) > 1 and not result[-1]:
            result.pop()

        return result[::-1]


tests = [
    [[1,1,1,1,1], [1,0,1], [1,0,0,0,0]],
    [[0], [0], [0]],
    [[1],[1],[1,1,0]]
]

run_functional_tests(Solution().addNegabinary, tests)
