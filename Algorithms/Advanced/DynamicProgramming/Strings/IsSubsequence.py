"""
https://leetcode.com/problems/is-subsequence/
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 108 ms, faster than 5.13% of Python3 online submissions for Is Subsequence.
Memory Usage: 13.7 MB, less than 94.77% of Python3 online submissions for Is Subsequence.
"""
"""
class Solution:

    def lcs(self, s: str, t: str):
        ns = len(s)
        nt = len(t)
        dp: List[List[int]] = [[0] * 2 for i in range(ns + 1)]
        for j in range(nt):
            j1 = j % 2
            j2 = (j + 1) % 2
            for i in range(ns):
                if s[i] == t[j]:
                    dp[i+1][j2] = 1 + dp[i][j1]
                else:
                    dp[i+1][j2] = max(dp[i][j2], dp[i+1][j1])
        return dp[ns][nt % 2]

    def isSubsequence(self, s: str, t: str) -> bool:
        return self.lcs(s, t) == len(s)
"""

"""
Runtime: 80 ms, faster than 6.25% of Python3 online submissions for Is Subsequence.
Memory Usage: 13.7 MB, less than 95.57% of Python3 online submissions for Is Subsequence.
"""
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        i = j = 0
        while i < ns and j < nt:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == ns


tests = [
    ["acb", "ahbgdc", False],
    ["abc", "ahbgdc", True],
    ["axc", "ahbgdc", False],
]

run_functional_tests(Solution().isSubsequence, tests)

