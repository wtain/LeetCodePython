"""
https://leetcode.com/problems/counting-words-with-a-given-prefix/

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.



Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.


Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 88 ms, faster than 5.21% of Python3 online submissions for Counting Words With a Given Prefix.
# Memory Usage: 13.9 MB, less than 73.40% of Python3 online submissions for Counting Words With a Given Prefix.
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for w in words if w[:len(pref)] == pref)


tests = [
    [["lewsmb","lewrydnve","lewqqm","lewec","lewn","lewb","lewedb"], "lew", 7],
    [["pay","attention","practice","attend"], "at", 2],
    [["leetcode","win","loops","success"], "code", 0]
]

run_functional_tests(Solution().prefixCount, tests)
