"""
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
import heapq
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 309
# ms
# Beats
# 97.29%
# of users with Python3
# Memory
# 33.30
# MB
# Beats
# 84.81%
# of users with Python3
# class Solution:
#     def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
#         cnt = Counter(arr)
#         counts = list(sorted(cnt.values()))
#         s = 0
#         n = len(counts)
#         for i in range(n):
#             if s + counts[i] <= k:
#                 s += counts[i]
#             else:
#                 return n-i
#         return 0


# Runtime
# 339
# ms
# Beats
# 68.75%
# of users with Python3
# Memory
# 33.40
# MB
# Beats
# 78.10%
# of users with Python3
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-16
# class Solution:
#     def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
#         cnt = Counter(arr)
#         counts = list(cnt.values())
#         heapq.heapify(counts)
#         s = 0
#         n = len(counts)
#         while counts:
#             s += heapq.heappop(counts)
#             if s > k:
#                 return len(counts) + 1
#         return 0


# Runtime
# 319
# ms
# Beats
# 89.69%
# of users with Python3
# Memory
# 33.24
# MB
# Beats
# 94.30%
# of users with Python3
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/editorial/?envType=daily-question&envId=2024-02-16
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        n = len(arr)
        count_of_frequencies = [0] * (n+1)
        for ci in cnt.values():
            count_of_frequencies[ci] += 1

        rem_unique = len(cnt)

        for i in range(1, n+1):
            to_remove = min(k // i, count_of_frequencies[i])
            k -= (i * to_remove)
            rem_unique -= to_remove
            if k < i:
                return rem_unique
        return 0


tests = [
    [[5,5,4], 1, 1],
    [[4,3,1,1,3,3,2], 3, 2],
]

run_functional_tests(Solution().findLeastNumOfUniqueInts, tests)
