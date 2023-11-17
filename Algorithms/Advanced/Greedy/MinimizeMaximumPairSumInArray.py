"""
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description/?envType=daily-question&envId=2023-11-17

The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.



Example 1:

Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
Example 2:

Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.


Constraints:

n == nums.length
2 <= n <= 105
n is even.
1 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 963
# ms
# Beats
# 87.96%
# of users with Python3
# Memory
# 30.84
# MB
# Beats
# 13.00%
# of users with Python3
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = nums[0] + nums[-1]
        n = len(nums)
        n2 = n // 2
        for i in range(1, n2):
            result = max(result, nums[i] + nums[n-1-i])
        return result


tests = [
    [[3,5,2,3], 7],
    [[3,5,4,2,4,6], 8],
]

run_functional_tests(Solution().minPairSum, tests)
