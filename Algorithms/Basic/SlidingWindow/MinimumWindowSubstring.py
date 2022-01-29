"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3891/
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import Counter, defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 720 ms, faster than 5.48% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 15 MB, less than 29.51% of Python3 online submissions for Minimum Window Substring.
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t or len(s) < len(t):
#             return ""
#         b, e = 0, len(t)-1
#         T = Counter(t)
#         S = Counter(s[:e+1])
#
#         def matches(S, T) -> bool:
#             for k in T:
#                 if S[k] < T[k]:
#                     return False
#             return True
#
#         result = ""
#         while e < len(s):
#             while matches(S, T) and b <= e:
#                 l = e - b + 1
#                 if not result or l < len(result):
#                     result = s[b:e+1]
#                 S[s[b]] -= 1
#                 b += 1
#             if e == len(s)-1:
#                 break
#             e += 1
#             S[s[e]] += 1
#             if matches(S, T):
#                 l = e - b + 1
#                 if not result or l < len(result):
#                     result = s[b:e + 1]
#         return result


# Runtime: 104 ms, faster than 74.93% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.8 MB, less than 87.81% of Python3 online submissions for Minimum Window Substring.
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if not s or not t or len(s) < len(t):
#             return ""
#         n, m = len(s), len(t)
#         chars = set(t)
#         b, e = 0, m-1
#         balance = defaultdict(int)
#         for i in range(m):
#             if s[i] in chars:
#                 balance[s[i]] += 1
#             balance[t[i]] -= 1
#
#         negatives = reduce(lambda v1, v2: v1+1, filter(lambda v: v < 0, balance.values()), 0)
#
#         result = ""
#         while e < len(s):
#             while negatives == 0 and b <= e:
#                 l = e - b + 1
#                 if not result or l < len(result):
#                     result = s[b:e+1]
#                 if s[b] in chars:
#                     if not balance[s[b]]:
#                         negatives += 1
#                     balance[s[b]] -= 1
#                 b += 1
#             if e == len(s)-1:
#                 break
#             e += 1
#             if s[e] in chars:
#                 if balance[s[e]] == -1:
#                     negatives -= 1
#                 balance[s[e]] += 1
#             if not negatives:
#                 l = e - b + 1
#                 if not result or l < len(result):
#                     result = s[b:e + 1]
#         return result


# Runtime: 128 ms, faster than 41.05% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 25.3 MB, less than 5.01% of Python3 online submissions for Minimum Window Substring.
# https://leetcode.com/problems/minimum-window-substring/solution/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        d_t = Counter(t)
        req = len(d_t)
        f_s = []
        for i, c in enumerate(s):
            if c in d_t:
                f_s.append((i, c))

        l, r = 0, 0
        formed = 0
        w_counts = defaultdict(int)
        res = float("inf"), None, None
        while r < len(f_s):
            ch = f_s[r][1]
            w_counts[ch] += 1

            if w_counts[ch] == d_t[ch]:
                formed += 1

            while l <= r and formed == req:
                ch = f_s[l][1]

                end = f_s[r][0]
                start = f_s[l][0]
                if end - start + 1 < res[0]:
                    res = end - start + 1, start, end
                w_counts[ch] -= 1
                if w_counts[ch] < d_t[ch]:
                    formed -= 1
                l += 1
            r += 1
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]


tests = [
    ["ADOBECODEBANC", "ABC", "BANC"],
    ["a", "a", "a"],
    ["a", "aa", ""]
]

# run_functional_tests(Solution().minWindow, tests, run_tests=[2])
run_functional_tests(Solution().minWindow, tests)