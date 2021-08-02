"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/
https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 124 ms, faster than 71.86% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.4 MB, less than 41.99% of Python3 online submissions for 3Sum Closest.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result, result_diff, n = 0, math.inf, len(nums)
        nums.sort()
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)
                if result_diff > diff:
                    result, result_diff = s, diff
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return result
        return result


tests = [
    [[-1,2,1,-4], 1, 2]
]

run_functional_tests(Solution().threeSumClosest, tests)