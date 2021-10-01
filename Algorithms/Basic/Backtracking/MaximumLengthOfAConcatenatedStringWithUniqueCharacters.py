"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3984/
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.



Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26


Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         n = len(arr)
#         max_len = 0
#
#         def impl(mask: int, curr_len: int, chars):
#             nonlocal max_len, n
#             max_len = max(max_len, curr_len)
#             for i in range(n):
#                 bit = 1 << i
#                 if mask & bit:
#                     continue
#                 chars_i = set(arr[i])
#                 if chars_i.intersection(chars):
#                     continue
#                 impl(mask | bit, curr_len + len(arr[i]), chars.union(chars_i))
#
#         impl(0, 0, set())
#
#         return max_len

# class Solution:
#     def maxLength(self, arr: List[str]) -> int:
#         n, max_len = len(arr), 0
#
#         chars = [set(arr[i]) for i in range(n)]
#
#         isect = [[0] * n for _ in range(n)]
#         for i in range(n):
#             isect[i][i] = 1
#         for i in range(n):
#             for j in range(i+1, n):
#                 if chars[i].intersection(chars[j]):
#                     isect[i][j] = isect[j][i] = 1
#
#         m = 1 << n
#         dp = [[0] * m]
#         dp[0] = 0
#         for i in range(n):
#             for j in range
#
#
#         return max(dp)


# Runtime: 76 ms, faster than 95.64% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Memory Usage: 14.5 MB, less than 43.78% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solution/
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        chars = list({self.to_bitset(w) for w in arr})
        return self.dfs(chars, 0, 0)

    def dfs(self, chars: List[int], pos: int, res: int) -> int:
        old_chars = res & ((1 << 26) - 1)
        old_len = res >> 26
        best = old_len

        for i in range(pos, len(chars)):
            new_chars = chars[i] & ((1 << 26) - 1)
            new_len = chars[i] >> 26
            if new_chars & old_chars:
                continue
            new_res = new_chars + old_chars + (new_len + old_len << 26)
            best = max(best, self.dfs(chars, i+1, new_res))
        return best

    def to_bitset(self, w: str) -> int:
        res = 0
        for c in w:
            o = ord(c) - ord('a')
            bit = 1 << o
            if res & bit:
                return 0
            res |= bit
        return res + (len(w) << 26)


tests = [
    [["un","iq","ue"], 4],
    [["cha","r","act","ers"], 6],
    [["abcdefghijklmnopqrstuvwxyz"], 26],
    [["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"], 16],
    [["yy","bkhwmpbiisbldzknpm"], 0]
]

run_functional_tests(Solution().maxLength, tests)