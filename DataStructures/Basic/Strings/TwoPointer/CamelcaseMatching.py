"""
https://leetcode.com/problems/camelcase-matching/

Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the query. You may insert each character at any position and you may not insert any characters.



Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".


Constraints:

1 <= pattern.length, queries.length <= 100
1 <= queries[i].length <= 100
queries[i] and pattern consist of English letters.

Given a single pattern and word, how can we solve it?
One way to do it is using a DP (pos1, pos2) where pos1 is a pointer to the word and pos2 to the pattern and returns true if we can match the pattern with the given word.
We have two scenarios: The first one is when `word[pos1] == pattern[pos2]`, then the transition will be just DP(pos1 + 1, pos2 + 1). The second scenario is when `word[pos1]` is lowercase then we can add this character to the pattern so that the transition is just DP(pos1 + 1, pos2) The case base is `if (pos1 == n && pos2 == m) return true;` Where n and m are the sizes of the strings word and pattern respectively.
"""
from typing import List

from Common.Constants import true, false
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
#         pattern = [c for c in pattern if str.isupper(c)]
#
#         def match(s: str) -> bool:
#             nonlocal pattern
#             return pattern == [c for c in s if str.isupper(c)]
#
#         return [match(s) for s in queries]


# XXX
# class Solution:
#     def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
#         m = len(pattern)
#
#         def match(s: str) -> bool:
#             nonlocal pattern, m
#             n = len(s)
#             dp = [[True] * (m+1) for _ in range(n+1)]
#             for i in range(n):
#                 for j in range(m):
#                     if s[i] == pattern[j]:
#                         dp[i+1][j+1] = dp[i][j]
#
#             return dp[-1][-1]
#
#         return [match(s) for s in queries]


# Runtime: 24 ms, faster than 96.47% of Python3 online submissions for Camelcase Matching.
# Memory Usage: 14.4 MB, less than 10.58% of Python3 online submissions for Camelcase Matching.
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        m = len(pattern)

        def match(s: str) -> bool:
            nonlocal pattern, m
            n = len(s)
            i, j = 0, 0
            while i < n and j < m:
                if s[i] == pattern[j]:
                    i += 1
                    j += 1
                elif s[i].isupper():
                    return False
                else:
                    i += 1
            if j < m:
                return False
            while i < n:
                if s[i].isupper():
                    return False
                i += 1
            return True

        return [match(s) for s in queries]


tests = [
    [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB", [true,false,true,true,false]],
    [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa", [true,false,true,false,false]],
    [["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT", [false,true,false,false,false]]
]

run_functional_tests(Solution().camelMatch, tests)
