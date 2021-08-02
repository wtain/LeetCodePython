"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""
import heapq
from collections import Counter, defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         n = len(s)
#         i1, i2 = 0, n-1
#         c = Counter(s)
#         # h = []
#         # for ch in c:
#         #     if c[ch] < k:
#
#         while i1 <= i2:
#             ch1, ch2 = s[i1], s[i2]
#             f = True
#             for ch in c:
#                 if c[ch] and c[ch] < k:
#                     f = False
#                     break
#             if f:
#                 return i2-i1+1
#             if c[ch1] < c[ch2]:
#                 c[ch1] -= 1
#                 i1 += 1
#             else:
#                 c[ch2] -= 1
#                 i2 -= 1
#         return 0


# Runtime: 164 ms, faster than 28.15% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# Memory Usage: 14.2 MB, less than 84.54% of Python3 online submissions for Longest Substring with At Least K Repeating Characters.
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def get_max_unique(s: str) -> int:
            c = set()
            max_uniq = 0
            n = len(s)
            for i in range(n):
                if s[i] not in c:
                    max_uniq += 1
                    c.add(s[i])
            return max_uniq

        mu = get_max_unique(s)
        result = 0

        for cu in range(1, mu+1):
            c = Counter()
            ws, we, i, uniq, cnt_at_least_k = 0, 0, 0, 0, 0
            while we < len(s):
                if uniq <= cu:
                    i = s[we]
                    if c[i] == 0:
                        uniq += 1
                    c[i] += 1
                    if c[i] == k:
                        cnt_at_least_k += 1
                    we += 1
                else:
                    i = s[ws]
                    if c[i] == k:
                        cnt_at_least_k -= 1
                    c[i] -= 1
                    if c[i] == 0:
                        uniq -= 1
                    ws += 1
                if uniq == cu and uniq == cnt_at_least_k:
                    result = max(we - ws, result)
        return result


tests = [
    ["bchhbbdefghiaaacb", 3, 3],
    ["aaabb", 3, 3],
    ["ababbc", 2, 5]
]

run_functional_tests(Solution().longestSubstring, tests)
