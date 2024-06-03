"""
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.


Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests

# WRONG
# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         n1, n2 = len(s), len(t)
#         j = 0
#         for i in range(n2):
#             while j < n1 and s[j] != t[i]:
#                 j += 1
#             if j == n1:
#                 return n2 - i
#         return 0


# Runtime
# 57
# ms
# Beats
# 73.64%
# of users with Python3
# Memory
# 17.60
# MB
# Beats
# 72.52%
# of users with Python3
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/editorial/?envType=daily-question&envId=2024-06-03
# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         first, longest_prefix = 0, 0
#
#         while first < len(s) and longest_prefix < len(t):
#             if s[first] == t[longest_prefix]:
#                 longest_prefix += 1
#             first += 1
#
#         return len(t) - longest_prefix



# Runtime
# 60
# ms
# Beats
# 64.70%
# of users with Python3
# Memory
# 17.44
# MB
# Beats
# 96.17%
# of users with Python3
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n1, n2 = len(s), len(t)
        i, j = 0, 0
        while i < n2:
            while j < n1 and s[j] != t[i]:
                j += 1
            if j == n1:
                return n2 - i
            i += 1
            j += 1
        return n2 - i


tests = [
    ["coaching", "coding", 4],
    ["abcde", "a", 0],
    ["z", "abcde", 5],
]

run_functional_tests(Solution().appendCharacters, tests)
