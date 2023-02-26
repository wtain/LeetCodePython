"""
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.



Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.


Constraints:

1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.


Follow up: Can you solve the problem in O(log(n)) time complexity?
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 128 ms
# Beats
# 70.64%
# Memory
# 14.2 MB
# Beats
# 51.59%
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i1, i2 = bisect.bisect_right(nums, -1), bisect.bisect_left(nums, 1)
        n = len(nums)
        return max(i1, n - i2)


tests = [
    [[-2,-1,-1,1,2,3], 3],
    [[-3,-2,-1,0,0,1,2], 3],
    [[5,20,66,1314], 4]
]

run_functional_tests(Solution().maximumCount, tests)
