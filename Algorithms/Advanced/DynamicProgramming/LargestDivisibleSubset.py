"""
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.



Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


# Runtime: 376 ms, faster than 77.84% of Python3 online submissions for Largest Divisible Subset.
# Memory Usage: 14.4 MB, less than 69.93% of Python3 online submissions for Largest Divisible Subset.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        counts, indexes = [1] * n, [-1] * n
        max_idx = 0
        for i in range(n):
            max_cnt = 1
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j]:
                    continue
                new_cnt = counts[j] + 1
                if new_cnt > max_cnt:
                    max_cnt = new_cnt
                    indexes[i] = j
            counts[i] = max_cnt
            if counts[i] > counts[max_idx]:
                max_idx = i
        result = []
        t = max_idx
        while t >= 0:
            result.append(nums[t])
            t = indexes[t]
        return result


tests = [
    [[1,2,3], [1,2]],
    [[1,2,4,8], [1,2,4,8]]
]

run_functional_tests(Solution().largestDivisibleSubset, tests, custom_check=compareSets)
