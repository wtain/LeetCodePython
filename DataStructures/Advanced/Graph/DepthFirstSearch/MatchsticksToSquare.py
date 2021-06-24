"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3780/
https://leetcode.com/problems/matchsticks-to-square/

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.



Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         s = sum(matchsticks)
#         l = s // 4
#         if l * 4 != s:
#             return False
#         sides = [0] * 4
#         n = len(matchsticks)
#         used = [False] * n
#         st = [[sides, used]]
#         while st:
#             sides, used = st.pop()
#             if all(s == l for s in sides):
#                 return True
#             for i in range(n):
#                 if used[i]:
#                     continue
#                 for j in range(4):
#                     if sides[j] + matchsticks[i] > l:
#                         continue
#                     sides1 = sides.copy()
#                     used1 = used.copy()
#                     sides1[j] += matchsticks[i]
#                     used1[i] = True
#                     st.append([sides1, used1])
#
#         return False


# Runtime: 432 ms, faster than 54.42% of Python3 online submissions for Matchsticks to Square.
# Memory Usage: 16.4 MB, less than 15.01% of Python3 online submissions for Matchsticks to Square.
# https://leetcode.com/problems/matchsticks-to-square/solution/
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s, n = sum(matchsticks), len(matchsticks)
        l = s // 4
        if l * 4 != s:
            return False
        memo = {}

        def solve(mask, sides_done):
            total = 0
            for i in range(n-1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[n - 1 - i]
            if total > 0 and total % l == 0:
                sides_done += 1
            if sides_done == 3:
                return True
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]
            res = False
            c = total // l
            rem = l * (c+1) - total
            for i in range(n - 1, -1, -1):
                if matchsticks[n-1-i] <= rem and mask & (1 << i):
                    if solve(mask ^ (1 << i), sides_done):
                        res = True
                        break
            memo[(mask, sides_done)] = res
            return res
        return solve((1 << n) - 1, 0)



tests = [
    [[1,7,4,4], False],

    [[5,5,5,5,4,4,4,4,3,3,3,3], True],
    [[1,1,2,2,2], True],
    [[3,3,3,3,4], False]
]

run_functional_tests(Solution().makesquare, tests)