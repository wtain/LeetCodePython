"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3690/
https://leetcode.com/problems/russian-doll-envelopes/

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

Return the maximum number of envelopes can you Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.



Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1


Constraints:

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
"""
from bisect import bisect_left
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         n = len(envelopes)
#         p = [[] for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
#                     p[i].append(j)
#         po = sorted([(-len(l), i) for i, l in enumerate(p)])
#         current = envelopes[po[0][1]]
#         cnt = 1
#         for i in range(1, n):
#             ei = envelopes[po[i][1]]
#             if current[0] < ei[0] and current[1] < ei[1]:
#                 cnt += 1
#                 current = ei
#         return cnt


# TLE
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         n = len(envelopes)
#         envelopes.sort()
#         dp = [1] * n
#         result = 1
#         for i in range(1, n):
#             for j in range(i):
#                 if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     result = max(result, dp[i])
#         return result


# Runtime: 148 ms, faster than 82.41% of Python3 online submissions for Russian Doll Envelopes.
# Memory Usage: 16.5 MB, less than 57.77% of Python3 online submissions for Russian Doll Envelopes.
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for (w,h) in envelopes:
            l = bisect_left(dp, h)
            if l == len(dp):
                dp.append(h)
            else:
                dp[l] = h
        return len(dp)


tests = [
    ([[8,3],[3,20],[15,5],[11,2],[19,6],[9,18],[1,19],[13,3],[14,20],[6,7]], 4),
    ([[5,4],[6,4],[6,7],[2,3]], 3),
    ([[1,1],[1,1],[1,1]], 1)
]

run_functional_tests(Solution().maxEnvelopes, tests)