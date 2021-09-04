"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".


Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 28 ms, faster than 85.60% of Python3 online submissions for Largest Substring Between Two Equal Characters.
# Memory Usage: 14.2 MB, less than 45.98% of Python3 online submissions for Largest Substring Between Two Equal Characters.
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_len = -1
        d = {}
        for i, c in enumerate(s):
            if c in d:
                len = i - d[c] - 1
                max_len = max(max_len, len)
            else:
                d[c] = i
        return max_len


tests = [
    ["mgntdygtxrvxjnwksqhxuxtrv", 18],
    ["aa", 0],
    ["abca", 2],
    ["cbzxy", -1],
    ["cabbac", 4]
]

run_functional_tests(Solution().maxLengthBetweenEqualCharacters, tests)