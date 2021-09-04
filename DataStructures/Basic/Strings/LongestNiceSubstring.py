"""
https://leetcode.com/problems/longest-nice-substring/

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.



Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
Example 4:

Input: s = "dDzeE"
Output: "dD"
Explanation: Both "dD" and "eE" are the longest nice substrings.
As there are multiple longest nice substrings, return "dD" since it occurs earlier.


Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 56 ms, faster than 60.63% of Python3 online submissions for Longest Nice Substring.
# Memory Usage: 14.3 MB, less than 63.25% of Python3 online submissions for Longest Nice Substring.
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result = ""
        n = len(s)
        for i in range(n):
            c1 = set()
            c2 = set()
            for j in range(i, n):
                if str.islower(s[j]):
                    c1.add(s[j])
                else:
                    c2.add(str.lower(s[j]))
                if c1 == c2:
                    ss = s[i:j+1]
                    if len(ss) > len(result):
                        result = ss

        return result


tests = [
    ["YazaAay", "aAa"],
    ["Bb", "Bb"],
    ["c", ""],
    ["dDzeE", "dD"]
]

run_functional_tests(Solution().longestNiceSubstring, tests)