"""
https://leetcode.com/problems/count-number-of-teams/

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4


Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         n = len(rating)
#         mins1, maxes1, mins2, maxes2 = [0] * n, [0] * n, [0] * n, [0] * n
#         mins1[0] = maxes1[0] = rating[0]
#         for i in range(1, n):
#             mins1[i] = min(mins1[i-1], rating[i])
#             maxes1[i] = max(maxes1[i-1], rating[i])
#         mins2[n-1] = maxes2[n-1] = rating[n-1]
#         for i in range(n-2, -1, -1):
#             mins2[i] = min(mins2[i + 1], rating[i])
#             maxes2[i] = max(maxes2[i + 1], rating[i])
#         result = 0
#         for i in range(1, n-1):
#             if mins1[i-1] < rating[i] < maxes2[i+1]:
#                 result += 1
#             if maxes1[i-1] > rating[i] > mins2[i+1]:
#                 result += 1
#         return result


# Runtime
# 122 ms
# Beats
# 94.10%
# Memory
# 14.8 MB
# Beats
# 5.31%
# https://leetcode.com/problems/count-number-of-teams/solutions/2448244/c-fenwick-tree/
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sorted = rating.copy()
        sorted.sort()
        fen = [0] * 100001

        def get_val(x):
            res = 0
            while x > 0:
                res += fen[x]
                x -= x & (-x)
            return res

        def add(x):
            while x < len(fen):
                fen[x] += 1
                x += x & (-x)

        result = cnt = 0
        n = len(rating)
        for x in rating:
            cnt += 1
            v = get_val(x)
            ind = bisect.bisect_left(sorted, x)
            rem = n - ind - (cnt - v)
            add(x)
            result += v * rem
            result += (cnt - v - 1) * (n - cnt - rem)
        return result


tests = [
    [[2,5,3,4,1], 3],
    [[2,1,3], 0],
    [[1,2,3,4], 4]
]

run_functional_tests(Solution().numTeams, tests)
