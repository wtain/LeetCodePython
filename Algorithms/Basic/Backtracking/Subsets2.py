"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3837/
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


# Runtime: 44 ms, faster than 30.36% of Python3 online submissions for Subsets II.
# Memory Usage: 14.4 MB, less than 57.33% of Python3 online submissions for Subsets II.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        codes = set()
        nums.sort()
        n = len(nums)
        m = 2 ** n
        for i in range(m):
            s = []
            code = 0
            for j in range(n):
                if i & (1 << j):
                    s.append(nums[j])
                    code *= (n+21)
                    code += nums[j] + 11
            if code in codes:
                continue
            result.append(s)
            codes.add(code)
        return result


tests = [
    [[4,4,4,1,4], [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]],
    [[1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]]],
    [[0], [[],[0]]]
]

run_functional_tests(Solution().subsetsWithDup, tests, custom_check=compareSets)