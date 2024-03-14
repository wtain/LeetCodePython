"""
https://leetcode.com/problems/binary-subarrays-with-sum/description/?envType=daily-question&envId=2024-03-14

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.



Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15


Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 221
# ms
# Beats
# 60.52%
# of users with Python3
# Memory
# 17.32
# MB
# Beats
# 87.31%
# of users with Python3
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n, result = len(nums), 0
        ilo, ihi = 0, 0
        sumlo, sumhi = 0, 0
        for j in range(n):
            sumlo += nums[j]
            while ilo < j and sumlo > goal:
                sumlo -= nums[ilo]
                ilo += 1

            sumhi += nums[j]

            while ihi < j and (sumhi > goal or sumhi == goal and nums[ihi] == 0):
                sumhi -= nums[ihi]
                ihi += 1

            if sumlo == goal:
                result += ihi - ilo + 1

        return result


tests = [
    [[1,0,1,0,1], 2, 4],
    [[0,0,0,0,0], 0, 15],
]

run_functional_tests(Solution().numSubarraysWithSum, tests)
