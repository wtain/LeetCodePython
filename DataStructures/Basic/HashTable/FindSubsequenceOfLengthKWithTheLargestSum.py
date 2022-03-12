"""
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation:
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7.
Another possible subsequence is [4, 3].


Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 71 ms, faster than 70.68% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
# Memory Usage: 14.2 MB, less than 86.10% of Python3 online submissions for Find Subsequence of Length K With the Largest Sum.
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = list(zip(nums[:k], list(range(k))))
        heapq.heapify(h)
        n = len(nums)
        for i in range(k, n):
            if h[0][0] < nums[i]:
                heapq.heappop(h)
                heapq.heappush(h, (nums[i], i))
        return [v for (i, v) in sorted((i, v) for (v, i) in h)]


tests = [
    [[2,1,3,3], 2, [3, 3]],
    [[-1,-2,3,4], 3, [-1,3,4]],
    [[3,4,3,3], 2, [3,4]]
]

run_functional_tests(Solution().maxSubsequence, tests)
