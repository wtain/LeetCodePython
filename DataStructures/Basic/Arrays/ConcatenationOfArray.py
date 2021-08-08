"""
https://leetcode.com/problems/concatenation-of-array/

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.



Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]


Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 88 ms, faster than 49.04% of Python3 online submissions for Concatenation of Array.
# Memory Usage: 14.5 MB, less than 81.79% of Python3 online submissions for Concatenation of Array.
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums


# Runtime: 80 ms, faster than 90.24% of Python3 online submissions for Concatenation of Array.
# Memory Usage: 14.7 MB, less than 23.20% of Python3 online submissions for Concatenation of Array.
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        for i in range(2*n):
            result[i] = nums[i % n]
        return result


tests = [
    [[1,2,1],  [1,2,1,1,2,1]],
    [[1,3,2,1], [1,3,2,1,1,3,2,1]]
]

run_functional_tests(Solution().getConcatenation, tests)