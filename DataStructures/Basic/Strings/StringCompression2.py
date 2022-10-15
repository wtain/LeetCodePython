"""
https://leetcode.com/problems/string-compression-ii/description/

Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.



Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.


Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.
"""
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3679 ms
# Beats
# 46.63%
# Memory
# 15.6 MB
# Beats
# 81.59%
# https://leetcode.com/problems/string-compression-ii/solutions/2704704/94-7-faster-top-down-dp-with-explanation/
# class Solution:
#     def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
#
#         dp = [[-1] * 101 for _ in range(101)]
#
#         def dfs(s: str, left: int, K: int):
#             nonlocal dp
#             k = K
#             if len(s) - left <= k:
#                 return 0
#             if dp[left][k] >= 0:
#                 return dp[left][k]
#             res = dfs(s, left+1, k-1) if k else 10000
#             c = 1
#             for i in range(left+1, len(s)+1):
#                 add_part = 0
#                 if c >= 100:
#                     add_part = 3
#                 elif c >= 10:
#                     add_part = 2
#                 elif c > 1:
#                     add_part = 1
#                 res = min(res, dfs(s, i, k) + 1 + add_part)
#                 if i == len(s):
#                     break
#                 if s[i] == s[left]:
#                     c += 1
#                 else:
#                     k -= 1
#                     if k < 0:
#                         break
#             dp[left][K] = res
#             return dp[left][K]
#
#         return dfs(s, 0, k)


# Runtime
# 2775 ms
# Beats
# 66.87%
# Memory
# 15.4 MB
# Beats
# 81.59%
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def dfs(s: str, left: int, K: int):
            k = K
            if len(s) - left <= k:
                return 0
            res = dfs(s, left+1, k-1) if k else 10000
            c = 1
            for i in range(left+1, len(s)+1):
                add_part = 0
                if c >= 100:
                    add_part = 3
                elif c >= 10:
                    add_part = 2
                elif c > 1:
                    add_part = 1
                res = min(res, dfs(s, i, k) + 1 + add_part)
                if i == len(s):
                    break
                if s[i] == s[left]:
                    c += 1
                else:
                    k -= 1
                    if k < 0:
                        break
            return res

        return dfs(s, 0, k)


tests = [
    ["aaabcccd", 2, 4],
    ["aabbaa", 2, 2],
    ["aaaaaaaaaaa", 0, 3]
]

run_functional_tests(Solution().getLengthOfOptimalCompression, tests)
