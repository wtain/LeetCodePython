"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.



Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.


Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 445ms
# Beats 94.01%of users with Python3
# Memory
# Details
# 20.74mb
# Beats 5.32%of users with Python3
class Solution:

    class Value:

        def __init__(self, l = 0, c = 1):
            self.Length = l
            self.Count = c

    class Node:

        def __init__(self, vmin, vmax):
            self.rangeMin = vmin
            self.rangeMax = vmax
            self.left = None
            self.right = None
            self.value = Solution.Value()

        def get_mid(self):
            return self.rangeMin + (self.rangeMax - self.rangeMin) // 2

        def get_left(self):
            if not self.left:
                self.left = Solution.Node(self.rangeMin, self.get_mid())
            return self.left

        def get_right(self):
            if not self.right:
                self.right = Solution.Node(self.get_mid()+1, self.rangeMax)
            return self.right

    def merge(self, v1: Value, v2: Value):
        if v1.Length == v2.Length:
            if not v1.Length:
                return Solution.Value()
            return Solution.Value(v1.Length, v1.Count+v2.Count)
        return v1 if v1.Length > v2.Length else v2

    def query(self, node: Node, num):
        if node.rangeMax <= num:
            return node.value
        elif node.rangeMin > num:
            return Solution.Value()
        else:
            return self.merge(self.query(node.get_left(), num), self.query(node.get_right(), num))

    def insert(self, node: Node, num, v: Value):
        if node.rangeMax == node.rangeMin:
            node.value = self.merge(v, node.value)
            return
        elif num <= node.get_mid():
            self.insert(node.get_left(), num, v)
        else:
            self.insert(node.get_right(), num, v)
        node.value = self.merge(node.get_left().value, node.get_right().value)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        vmin, vmax = min(nums), max(nums)
        root = Solution.Node(vmin, vmax)
        for num in nums:
            v = self.query(root, num-1)
            self.insert(root, num, Solution.Value(v.Length+1, v.Count))
        return root.value.Count


tests = [
    [[1,3,5,4,7], 2],
    [[2,2,2,2,2], 5],
]

run_functional_tests(Solution().findNumberOfLIS, tests)
