"""
https://leetcode.com/problems/number-of-wonderful-substrings/

A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"


Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def wonderfulSubstrings(self, word: str) -> int:
#         result = 0
#         n = len(word)
#         codes = [0] * n
#         for i in range(n):
#             codes[i] = 1 << (ord(word[i]) - ord('a'))
#
#         def ispower2(x):
#             return x > 0 and x & (x-1) == 0
#
#         seen = defaultdict(int)
#         ps = 0
#         for i in range(n):
#             ps ^= codes[i]
#             if ps == 0 or ispower2(ps):
#                 result += 1
#             result += seen[ps]
#             for ps1 in seen:
#                 if ispower2(ps ^ ps1):
#                     result += seen[ps1]
#             seen[ps] += 1
#
#         return result


# Runtime
# 2933 ms
# Beats
# 32.31%
# Memory
# 17.2 MB
# Beats
# 6.15%
# class Solution:
#     def wonderfulSubstrings(self, word: str) -> int:
#         result = 0
#         n = len(word)
#         codes = [0] * n
#         for i in range(n):
#             codes[i] = 1 << (ord(word[i]) - ord('a'))
#
#         def ispower2(x):
#             return x > 0 and x & (x-1) == 0
#
#         seen = defaultdict(int)
#         ps = 0
#         for i in range(n):
#             ps ^= codes[i]
#             if ps == 0 or ispower2(ps):
#                 result += 1
#             result += seen[ps]
#             for j in range(10):
#                 mask = 1 << j
#                 ps1 = ps ^ mask
#                 result += seen[ps1]
#             seen[ps] += 1
#
#         return result


# Runtime
# 2646 ms
# Beats
# 52.31%
# Memory
# 15.1 MB
# Beats
# 52.31%
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        result = 0
        n = len(word)

        seen = defaultdict(int)
        seen[0] = 1
        ps = 0
        for i in range(n):
            ps ^= 1 << (ord(word[i]) - ord('a'))
            result += seen[ps]
            for j in range(10):
                mask = 1 << j
                ps1 = ps ^ mask
                result += seen[ps1]
            seen[ps] += 1

        return result


tests = [
    ["ehaehcjjaafjdceac", 29],
    ["aba", 4],
    ["aabb", 9],
    ["he", 2],
]

run_functional_tests(Solution().wonderfulSubstrings, tests)
