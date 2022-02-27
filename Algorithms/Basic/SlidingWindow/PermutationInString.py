"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# https://leetcode.com/submissions/detail/341160769/
# Runtime: 124 ms, faster than 50.00% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.1 MB, less than 73.45% of Python3 online submissions for Permutation in String.
class Solution:

    class Hist:

        def __init__(self):
            self.h = defaultdict(int)
            self.dist = 0

        def add(self, c):
            self.dist -= abs(self.h.get(c, 0))
            self.h[c] += 1
            self.dist += abs(self.h.get(c, 0))

        def remove(self, c):
            self.dist -= abs(self.h.get(c, 0))
            self.h[c] -= 1
            self.dist += abs(self.h.get(c, 0))

        def is_zero_distance(self):
            return self.dist == 0

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        if n < m:
            return False

        h = self.Hist()
        for i in range(m):
            h.remove(s1[i])
            h.add(s2[i])

        if h.is_zero_distance():
            return True

        i1 = 0
        for i2 in range(m, n):
            h.remove(s2[i1])
            h.add(s2[i2])
            if h.is_zero_distance():
                return True
            i1 += 1

        return False


tests = [
    ["ab", "eidbaooo", True],
    ["ab", "eidboaoo", False]
]

run_functional_tests(Solution().checkInclusion, tests)
