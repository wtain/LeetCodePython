"""
https://leetcode.com/problems/get-equal-substrings-within-budget/description/?envType=daily-question&envId=2024-05-28

You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.



Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.


Constraints:

1 <= s.length <= 105
t.length == s.length
0 <= maxCost <= 106
s and t consist of only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 69
# ms
# Beats
# 34.07%
# of users with Python3
# Memory
# 17.30
# MB
# Beats
# 34.48%
# of users with Python3
# https://leetcode.com/problems/get-equal-substrings-within-budget/editorial/?envType=daily-question&envId=2024-05-28
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        max_len = 0
        start, cur_cost = 0, 0
        for i in range(n):
            cur_cost += abs(ord(s[i]) - ord(t[i]))

            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            max_len = max(max_len, i - start + 1)
        return max_len


tests = [
    ["abcd", "bcdf", 3, 3],
    ["abcd", "cdef", 3, 1],
    ["abcd", "acde", 0, 1],
]

run_functional_tests(Solution().equalSubstring, tests)
