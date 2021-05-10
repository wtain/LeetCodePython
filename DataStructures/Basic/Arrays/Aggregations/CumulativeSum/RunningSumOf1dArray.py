"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3730/
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.



Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
from itertools import accumulate
from typing import List



from Common.ObjectTestingUtils import run_functional_tests
import numpy


# Runtime: 96 ms, faster than 5.06% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 31.2 MB, less than 13.13% of Python3 online submissions for Running Sum of 1d Array.
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         return list(numpy.cumsum(nums))


# Runtime: 40 ms, faster than 61.92% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.4 MB, less than 43.79% of Python3 online submissions for Running Sum of 1d Array.
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i-1]
#         return nums


# Runtime: 40 ms, faster than 61.92% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.2 MB, less than 90.18% of Python3 online submissions for Running Sum of 1d Array.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


tests = [
    [
        [1,2,3,4],
        [1,3,6,10]
    ],
    [
        [1,1,1,1,1],
        [1,2,3,4,5]
    ],
    [
        [3,1,2,10,1],
        [3,4,6,16,17]
    ]
]

run_functional_tests(Solution().runningSum, tests)