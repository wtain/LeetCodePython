"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609/
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


# Runtime: 6140 ms, faster than 22.21% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 21.9 MB, less than 18.80% of Python3 online submissions for Longest Palindromic Substring.
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for i in range(n)]
#         result = ""
#         for i in range(n):
#             dp[i][i] = True
#             if len(result) < 1:
#                 result = s[i]
#             if i < n-1 and s[i+1] == s[i]:
#                 dp[i][i+1] = True
#                 if len(result) < 2:
#                     result = s[i:i+2]
#
#         for l in range(3, n+1):
#             for i in range(n-l+1):
#                 j = i+l-1
#                 if dp[i+1][j-1] and s[i] == s[j]:
#                     dp[i][j] = True
#                     if len(result) < l:
#                         result = s[i:j+1]
#
#         return result

# https://hackernoon.com/manachers-algorithm-explained-longest-palindromic-substring-22cb27a5e96f
# https://wiki2.org/en/Longest_palindromic_substring#Manacher's_algorithm

# Runtime: 152 ms, faster than 95.46% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.5 MB, less than 40.05% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def getModifiedString(s: str) -> str:
            res = ""
            for c in s:
                res += "#" + c
            res += "#"
            return res

        S = getModifiedString(s)
        L = 2 * n + 1
        P = [0] * L
        c = 0
        r = 0
        maxLen = 0
        result = ""
        for i in range(L):
            mirror = (2*c) - i
            if i < r:
                P[i] = min(r - i, P[mirror])
            a = i + (1 + P[i])
            b = i - (1 + P[i])
            while a < L and b >= 0 and S[a] == S[b]:
                P[i] += 1
                a += 1
                b -= 1

            if i + P[i] > r:
                c = i
                r = i + P[i]

                if P[i] > maxLen:
                    maxLen = P[i]
                    result = S[i-maxLen:i+maxLen+1]
        return result.replace("#", "")


tests = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("ac", "a")
]

for test in tests:
    result = Solution().longestPalindrome(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + result)