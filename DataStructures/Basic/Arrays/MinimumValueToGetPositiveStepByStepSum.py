"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.



Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2
Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.
Example 3:

Input: nums = [1,-2,-3]
Output: 5


Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
from functools import reduce
from typing import List


# Runtime: 32 ms, faster than 70.34% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14.3 MB, less than 45.48% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Runtime: 20 ms, faster than 99.55% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14.1 MB, less than 75.22% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# class Solution:
#     def minStartValue(self, nums: List[int]) -> int:
#         s = 0
#         mins = 0
#         for a in nums:
#             s += a
#             mins = min(s, mins)
#         # startV + mins >= 1
#         # startV >= 1 - mins
#         return max(1 - mins, 1)
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 73.73% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14.4 MB, less than 9.55% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(1 - reduce(lambda r, a: (r[0]+a, min(r[0]+a, r[1])), nums, (0, 0))[1], 1)


tests = [
    [[-3,2,-3,4,2], 5],
    [[1,2], 1],
    [[1,-2,-3], 5]
]

run_functional_tests(Solution().minStartValue, tests)
