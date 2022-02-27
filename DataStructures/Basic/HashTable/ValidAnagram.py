"""
https://leetcode.com/problems/valid-anagram/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from typing import Dict

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 64 ms, faster than 32.90% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.2 MB, less than 40.11% of Python3 online submissions for Valid Anagram.
Runtime: 52 ms, faster than 54.27% of Python3 online submissions for Valid Anagram.
Memory Usage: 14.5 MB, less than 48.96% of Python3 online submissions for Valid Anagram.
"""
class Solution:

    @staticmethod
    def getHist(s: str) -> Dict[chr, int]:
        result: Dict[chr, int] = {}
        for c in s:
            if result.get(c):
                result[c] += 1
            else:
                result[c] = 1
        return result

    @staticmethod
    def compareHists(h1: Dict[chr, int], h2: Dict[chr, int]) -> bool:
        for k, v in h1.items():
            if not h2.get(k) or h2[k] != v:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        h1 = Solution.getHist(s)
        h2 = Solution.getHist(t)
        if len(h1) != len(h2):
            return False
        return Solution.compareHists(h1, h2)


tests = [
    ["anagram", "nagaram", True],
    ["rat", "car", False]
]

run_functional_tests(Solution().isAnagram, tests)
