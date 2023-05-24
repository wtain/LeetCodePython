"""
https://leetcode.com/problems/maximum-subsequence-score/description/

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

For chosen indices i0, i1, ..., ik - 1, your score is defined as:

The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.

A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.



Example 1:

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation:
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
Example 2:

Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation:
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.


Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
0 <= nums1[i], nums2[j] <= 105
1 <= k <= n
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         arr = list(sorted([b, a] for a, b in zip(nums1, nums2)))
#         return 0

# Runtime
# 1082 ms
# Beats
# 40.8%
# Memory
# 40.4 MB
# Beats
# 12.98%
# https://leetcode.com/problems/maximum-subsequence-score/editorial/
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [[a, b] for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])
        h = [x[0] for x in pairs[:k]]
        s = sum(h)
        heapq.heapify(h)
        result = s * pairs[k-1][1]
        for i in range(k, len(pairs)):
            s -= heapq.heappop(h)
            s += pairs[i][0]
            heapq.heappush(h, pairs[i][0])
            result = max(result, s * pairs[i][1])
        return result


tests = [
    [[1,3,3,2], [2,1,3,4], 3, 12],
    [[4,2,3,1,1], [7,5,10,9,6], 1, 30],
]

run_functional_tests(Solution().maxScore, tests)
