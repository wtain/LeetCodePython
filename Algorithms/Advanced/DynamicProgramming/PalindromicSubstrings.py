"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3686/
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:

The input string length won't exceed 1000.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 244 ms, faster than 49.40% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 21.8 MB, less than 39.18% of Python3 online submissions for Palindromic Substrings.
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            cnt += 1
            if i > 0 and s[i-1] == s[i]:
                dp[i-1][i] = True
                cnt += 1

        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    cnt += 1

        return cnt


tests = [
    ("abc", 3),
    ("aaa", 6)
]

run_functional_tests(Solution().countSubstrings, tests)