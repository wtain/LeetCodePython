"""
https://leetcode.com/problems/permutations/submissions/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 35ms
# Beats 99.72%of users with Python3
# Memory
# Details
# 16.74mb
# Beats 13.68%of users with Python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        n = len(nums)
        used = [False] * n

        r = []

        def impl():
            for i in range(n):
                if used[i]:
                    continue
                r.append(nums[i])
                if len(r) == n:
                    results.append(r.copy())
                else:
                    used[i] = True
                    impl()
                    used[i] = False
                r.pop()

        impl()

        return results


tests = [
    [[1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]],
    [[0,1], [[0,1],[1,0]]],
    [[1], [[1]]],
]

run_functional_tests(Solution().permute, tests)
