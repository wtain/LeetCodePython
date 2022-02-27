"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 137 ms, faster than 70.79% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.3 MB, less than 41.94% of Python3 online submissions for Find All Anagrams in a String.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hist, dist = defaultdict(int), 0

        def add(c, delta):
            nonlocal hist, dist
            dist -= abs(hist[c])
            hist[c] += delta
            dist += abs(hist[c])

        n, m, result = len(s), len(p), []
        if n < m:
            return result

        for i in range(m):
            add(p[i], -1)
            add(s[i], 1)
        if not dist:
            result.append(0)

        for i1 in range(n-m):
            i2 = i1 + m
            add(s[i1], -1)
            add(s[i2], 1)
            if not dist:
                result.append(i1+1)

        return result


tests = [
    ["cbaebabacd", "abc", [0,6]],
    ["abab", "ab", [0,1,2]]
]

run_functional_tests(Solution().findAnagrams, tests)
