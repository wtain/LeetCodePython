"""
https://leetcode.com/problems/longest-ideal-subsequence/

You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.



Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.


Constraints:

1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3391 ms
# Beats
# 9.28%
# Memory
# 14.7 MB
# Beats
# 26.43%
# class Solution:
#     def longestIdealString(self, s: str, k: int) -> int:
#         result = 0
#         ends = defaultdict(int)
#         for c in s:
#             l = max(ends[chr(ord(c) + d)]+1 for d in range(-k, k+1) if 0 <= ord(c) - ord('a') + d < 26)
#             ends[c] = max(ends[c], l)
#             result = max(result, ends[c])
#         return result

# Runtime
# 830 ms
# Beats
# 55%
# Memory
# 14.7 MB
# Beats
# 26.43%
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        result = 0
        dp = [0] * 26
        for c in s:
            o = ord(c) - ord('a')
            l = max(dp[max(o-k, 0):min(o+k+1, 26)]) + 1
            dp[o] = max(dp[o], l)
            result = max(result, dp[o])
        return result


tests = [
    ["acfgbd", 2, 4],
    ["abcd", 3, 4],
]

run_functional_tests(Solution().longestIdealString, tests)
