"""
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/

You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         MOD = 10 ** 9 + 7
#         m = len(words)
#
#         def dp(k, j):
#             if k == len(target):
#                 return 0
#             result = 0
#             for i in range(m):
#                 if k < len(words[i]) and target[j] == words[i][k]:
#                     result += dp(k+1, j+1)
#             result += dp(k + 1, j)
#             return result
#
#         return dp(0, 0) % MOD


# Runtime
# 3742 ms
# Beats
# 10.12%
# Memory
# 39 MB
# Beats
# 70.4%
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/editorial/
# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         MOD = 10 ** 9 + 7
#         ALPHABET = 26
#         m = len(target)
#         k = len(words[0])
#         cnt = [[0] * k for _ in range(ALPHABET)]
#         for j in range(k):
#             for word in words:
#                 cnt[ord(word[j])-ord('a')][j] += 1
#         dp = [[0] * (k+1) for _ in range(m+1)]
#         dp[0][0] = 1
#         for i in range(m+1):
#             for j in range(k):
#                 if i < m:
#                     dp[i+1][j+1] += cnt[ord(target[i]) - ord('a')][j] * dp[i][j]
#                     dp[i + 1][j + 1] %= MOD
#                 dp[i][j+1] += dp[i][j]
#                 dp[i][j + 1] %= MOD
#         return dp[-1][-1]

# Runtime
# 2685 ms
# Beats
# 39.30%
# Memory
# 388.5 MB
# Beats
# 7.78%
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/editorial/
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        ALPHABET = 26
        m, k = len(target), len(words[0])
        cnt = [[0] * k for _ in range(ALPHABET)]
        for j in range(k):
            for word in words:
                cnt[ord(word[j])-ord('a')][j] += 1

        @cache
        def dp(i, j):
            if j == 0:
                return 1 if i == 0 else 0
            result = dp(i, j-1)
            if i > 0:
                result += cnt[ord(target[i-1])-ord('a')][j-1] * dp(i-1, j-1)
            result %= MOD
            return result

        return dp(m, k)


tests = [
    [["acca","bbbb","caca"], "aba", 6],
    [["abba","baab"], "bab", 4],
]

run_functional_tests(Solution().numWays, tests)
