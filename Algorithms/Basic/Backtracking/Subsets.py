"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 46 ms, faster than 49.95% of Python3 online submissions for Subsets.
# Memory Usage: 14.1 MB, less than 95.43% of Python3 online submissions for Subsets.
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         results = []
#         n = len(nums)
#         for mask in range(1 << n):
#             subset = []
#             for j in range(n):
#                 if mask & (1 << j):
#                     subset.append(nums[j])
#             results.append(subset)
#         return results


# Runtime: 54 ms, faster than 34.06% of Python3 online submissions for Subsets.
# Memory Usage: 14.1 MB, less than 95.43% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        n = len(nums)

        for i in range(n):
            m = len(results)
            for j in range(m):
                results.append(results[j] + [nums[i]])

        return results


tests = [
    [[1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]],
    [[0], [[],[0]]]
]

run_functional_tests(Solution().subsets, tests)
