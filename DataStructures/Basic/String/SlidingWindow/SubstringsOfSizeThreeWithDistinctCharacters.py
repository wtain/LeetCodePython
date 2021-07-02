"""
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.
"""
from collections import Counter, defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 86.20% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
# Memory Usage: 14.1 MB, less than 71.84% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt, n, l, r = 0, len(s), 0, 0
        if n < 3:
            return 0
        win = defaultdict(int)
        for i in range(3):
            win[s[r]] += 1
            r += 1
        if len(win) == 3:
            cnt += 1
        for r in range(3, n):
            win[s[l]] -= 1
            if win[s[l]] == 0:
                del win[s[l]]
            l += 1
            win[s[r]] += 1
            if len(win) == 3:
                cnt += 1
        return cnt


tests = [
    ["x", 0],
    ["xyzzaz", 1],
    ["aababcabc", 4]
]

run_functional_tests(Solution().countGoodSubstrings, tests)