"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.



Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 104
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1158 ms
# Beats
# 37.8%
# Memory
# 42.9 MB
# Beats
# 8.22%
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        if not nums1:
            return []

        i1 = 0
        h = []
        for i2 in range(len(nums2)):
            heapq.heappush(h, (nums1[i1] + nums2[i2], i1, i2))

        while len(result) < k and h:
            v, i1, i2 = heapq.heappop(h)
            result.append([nums1[i1], nums2[i2]])
            i1 += 1
            if i1 < len(nums1):
                heapq.heappush(h, (nums1[i1] + nums2[i2], i1, i2))

        return result


tests = [
    [[1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]],
    [[1,1,2], [1,2,3], 2, [[1,1],[1,1]]],
    [[1,2], [3], 3, [[1,3],[2,3]]],
]

run_functional_tests(Solution().kSmallestPairs, tests)
