"""
https://leetcode.com/problems/palindrome-partitioning/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3565/
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

Runtime: 636 ms, faster than 10.95% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 32.7 MB, less than 5.29% of Python3 online submissions for Palindrome Partitioning.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 919 ms, faster than 9.97% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 32.4 MB, less than 8.53% of Python3 online submissions for Palindrome Partitioning.
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         result = []
#
#         n = len(s)
#         p: List[List[bool]] = [[False] * n for i in range(n)]
#         for i in range(n):
#             p[i][i] = True
#             if i+1 < n and s[i] == s[i+1]:
#                 p[i][i+1] = True
#
#         for l in range(3, n+1):
#             for i in range(n-l+1):
#                 j = i + l - 1
#                 if p[i+1][j-1] and s[i] == s[j]:
#                     p[i][j] = True
#
#         def dfs(i: int, current: List[str]):
#             if i == n:
#                 result.append(current)
#             else:
#                 for j in range(i, n):
#                     if p[i][j]:
#                         new = current[:]
#                         new.append(s[i:j+1])
#                         dfs(j+1, new)
#
#         dfs(0, [])
#
#         return result


# Runtime
# 638 ms
# Beats
# 95.26%
# Memory
# 30.4 MB
# Beats
# 46.86%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        n = len(s)
        p = [[False] * n for i in range(n)]
        for i in range(n):
            p[i][i] = True
            if i+1 < n and s[i] == s[i+1]:
                p[i][i+1] = True

        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if p[i+1][j-1] and s[i] == s[j]:
                    p[i][j] = True

        current = []

        def dfs(i: int):
            nonlocal current
            if i == n:
                result.append(current.copy())
            else:
                for j in range(i, n):
                    if p[i][j]:
                        current.append(s[i:j+1])
                        dfs(j+1)
                        current.pop()

        dfs(0)

        return result


tests = [
    [
        "efe",
        [["e","f","e"],["efe"]]
    ],
    [
        "aaba",
        [['a', 'a', 'b', 'a'], ['a', 'aba'], ['aa', 'b', 'a']]
    ],
    [
        "aab",
        [["a","a","b"],["aa","b"]]
    ],
    [
        "a",
        [["a"]]
    ]
]

run_functional_tests(Solution().partition, tests)
