"""
https://leetcode.com/problems/range-sum-query-immutable/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3892/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests

"""
Runtime: 160 ms, faster than 35.24% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.5 MB, less than 24.00% of Python3 online submissions for Range Sum Query - Immutable.
Runtime: 80 ms, faster than 62.86% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.7 MB, less than 62.73% of Python3 online submissions for Range Sum Query - Immutable.
"""
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        if n == 0:
            return
        self.ps = [0] * n
        self.ps[0] = nums[0]
        for i in range(1, n):
            self.ps[i] = self.ps[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        result = self.ps[j]
        if i > 0:
            result -= self.ps[i-1]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

tests = [
    [
        ["NumArray", "sumRange", "sumRange", "sumRange"],
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]],
        [null, 1, -1, -3]
    ],
    [
        ["NumArray"],
        [[[]]],
        [null]
    ]
]

run_object_tests(tests, cls=NumArray)
