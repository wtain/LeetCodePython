"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.



Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


# Runtime: 404 ms, faster than 38.51% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 21.5 MB, less than 92.66% of Python3 online submissions for Find All Duplicates in an Array.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] != nums[nums[i] - 1]:
                ni = nums[i]
                nums[i], nums[ni-1] = nums[ni-1], nums[i]
            else:
                i += 1
        return [nums[i] for i in range(n) if nums[i] != i+1]


tests = [
    [[4,3,2,7,8,2,3,1], [2,3]],
    [[1,1,2], [1]],
    [[1], []]
]

run_functional_tests(Solution().findDuplicates, tests, custom_check=compareSets)