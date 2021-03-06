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


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        n = len(s)
        p: List[List[bool]] = [[False] * n for i in range(n)]
        for i in range(n):
            p[i][i] = True
            if i+1 < n and s[i] == s[i+1]:
                p[i][i+1] = True

        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if p[i+1][j-1] and s[i] == s[j]:
                    p[i][j] = True

        def dfs(i: int, current: List[str]):
            if i == n:
                result.append(current)
            else:
                for j in range(i, n):
                    if p[i][j]:
                        new = current[:]
                        new.append(s[i:j+1])
                        dfs(j+1, new)

        dfs(0, [])

        return result


print(Solution().partition("efe"))  # [["e","f","e"],["efe"]]
print(Solution().partition("aaba"))  # [['a', 'a', 'b', 'a'], ['a', 'aba'], ['aa', 'b', 'a']]
print(Solution().partition("aab"))  # [["a","a","b"],["aa","b"]]
print(Solution().partition("a"))  # [["a"]]

