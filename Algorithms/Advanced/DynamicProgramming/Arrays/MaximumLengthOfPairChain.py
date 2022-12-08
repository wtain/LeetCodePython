"""
https://leetcode.com/problems/maximum-length-of-pair-chain/

ou are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.



Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].


Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
"""
import operator
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2897 ms
# Beats
# 25.12%
# Memory
# 14.4 MB
# Beats
# 83.87%
# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort()
#         n = len(pairs)
#         dp = [1] * n
#         for i in range(1, n):
#             for j in range(i):
#                 if pairs[j][1] < pairs[i][0]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return dp[-1]



# Runtime
# 8228 ms
# Beats
# 5.7%
# Memory
# 14.5 MB
# Beats
# 41.59%
# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort()
#         n = len(pairs)
#         dp = [1] * n
#         for i in range(1, n):
#             for j in range(i):
#                 if pairs[j][1] < pairs[i][0]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)


# TLE??
# class Solution:
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort()
#         n = len(pairs)
#         dp = [1] * n
#         result = 1
#         for i in range(1, n):
#             for j in range(i):
#                 if pairs[j][1] < pairs[i][0]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#                     result = max(result, dp[i])
#         return result


# Runtime
# 223 ms
# Beats
# 91.24%
# Memory
# 14.3 MB
# Beats
# 83.87%
# https://leetcode.com/problems/maximum-length-of-pair-chain/solutions/127487/maximum-length-of-pair-chain/
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        current, result = float("-inf"), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if current < x:
                current = y
                result += 1
        return result


tests = [
    [[[1,2],[2,3],[3,4]], 2],
    [[[1,2],[7,8],[4,5]], 3]
]

run_functional_tests(Solution().findLongestChain, tests)
