"""
https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.



Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0


Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         v1, v2 = arrays[0][0], arrays[0][-1]
#         n = len(arrays)
#         for i in range(1, n):
#             v1 = min(v1, arrays[i][0])
#             v2 = max(v2, arrays[i][-1])
#         return v2 - v1

# TLE
# class Solution:
#     def maxDistance(self, arrays: List[List[int]]) -> int:
#         n = len(arrays)
#         max_dist = 0
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 max_dist = max(max_dist, arrays[j][-1] - arrays[i][0])
#         return max_dist


# Runtime
# 1374
# ms
# Beats
# 30.75%
# Analyze Complexity
# Memory
# 42.42
# MB
# Beats
# 63.79%
# https://leetcode.com/problems/maximum-distance-in-arrays/solutions/5642927/easy-greedy-solution-beats-100/?envType=daily-question&envId=2024-08-16
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        v1, v2 = arrays[0][0], arrays[0][-1]
        n = len(arrays)
        max_dist = 0
        for i in range(1, n):
            max_dist = max(max_dist, arrays[i][-1] - v1, v2 - arrays[i][0])
            v1 = min(v1, arrays[i][0])
            v2 = max(v2, arrays[i][-1])
        return max_dist


tests = [
    [[[1,4],[0,5]], 4],
    [[[1,2,3],[4,5],[1,2,3]], 4],
    [[[1],[1]], 0],
]

run_functional_tests(Solution().maxDistance, tests)
