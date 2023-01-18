"""
https://leetcode.com/problems/maximum-sum-circular-subarray/description/

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.



Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.


Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 760 ms
# Beats
# 41.1%
# Memory
# 19.8 MB
# Beats
# 5.49%
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        P = [0] * (2*n+1)
        for i in range(2*n):
            P[i+1] = P[i] + nums[i % n]
        ind = deque([0])
        for j in range(1, 2*n+1):
            while ind[0] < j - n:
                ind.popleft()
            result = max(result, P[j] - P[ind[0]])
            while ind and P[j] <= P[ind[-1]]:
                ind.pop()
            ind.append(j)
        return result


tests = [
    [[1,-2,3,-2], 3],
    [[5,-3,5], 10],
    [[-3,-2,-3], -2],
]

run_functional_tests(Solution().maxSubarraySumCircular, tests)