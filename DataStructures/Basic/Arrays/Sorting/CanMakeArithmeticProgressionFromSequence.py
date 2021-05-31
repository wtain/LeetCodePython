"""
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.



Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Constraints:

2 <= arr.length <= 1000
-106 <= arr[i] <= 106
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 64 ms, faster than 6.05% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
# Memory Usage: 14.4 MB, less than 63.09% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         arr = sorted(arr)
#         diff = arr[1] - arr[0]
#         n = len(arr)
#         for i in range(2, n):
#             if arr[i] - arr[i-1] != diff:
#                 return False
#         return True

# Runtime: 48 ms, faster than 7.17% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
# Memory Usage: 14.6 MB, less than 5.86% of Python3 online submissions for Can Make Arithmetic Progression From Sequence.
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        amin, amax = min(arr), max(arr)
        n = len(arr)
        diff = (amax - amin) // (n - 1)
        if diff == 0:
            return True
        multiples = set()
        for i in range(n):
            di = arr[i] - amin
            if di % diff != 0:
                return False
            m = di // diff
            if m < 0 or m > n-1:
                return False
            if m in multiples:
                return False
            multiples.add(m)
        return True


tests = [
    [[3,5,1], True],
    [[1,2,4], False]
]

run_functional_tests(Solution().canMakeArithmeticProgression, tests)