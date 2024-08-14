"""
https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/?envType=daily-question&envId=2024-08-14

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.



Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5


Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 76
# ms
# Beats
# 97.65%
# Analyze Complexity
# Memory
# 17.54
# MB
# Beats
# 16.16%
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mi = lo + (hi-lo) // 2
            count, left = 0, 0
            for j in range(n):
                while nums[j] - nums[left] > mi:
                    left += 1
                count += j - left
            if count < k:
                lo = mi + 1
            else:
                hi = mi
        return lo


tests = [
    [[1,3,1], 1, 0],
    [[1,1,1], 2, 0],
    [[1,6,1], 3, 5],
]

run_functional_tests(Solution().smallestDistancePair, tests)
