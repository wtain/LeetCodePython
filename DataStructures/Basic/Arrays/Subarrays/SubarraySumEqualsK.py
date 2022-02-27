"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000git comm
-107 <= k <= 107
"""
from typing import List


# Runtime: 268 ms
# Memory Usage: 16.6 MB
# Runtime: 276 ms, faster than 63.16% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.6 MB, less than 93.61% of Python3 online submissions for Subarray Sum Equals K.
# Runtime: 264 ms, faster than 47.76% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.9 MB, less than 28.60% of Python3 online submissions for Subarray Sum Equals K.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        counts = {}
        s = 0
        for i in range(n):
            s += nums[i]
            if s == k:
                cnt += 1
            cnt += counts.get(s - k, 0)
            counts[s] = counts.get(s, 0) + 1
        return cnt


tests = [
    [[1,1,1], 2, 2],
    [[1,2,3], 3, 2]
]

run_functional_tests(Solution().subarraySum, tests)
