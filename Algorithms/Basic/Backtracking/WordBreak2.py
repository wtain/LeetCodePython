"""
https://leetcode.com/problems/word-break-ii/description/?envType=daily-question&envId=2024-05-25

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
"""
from functools import cache
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 36
# ms
# Beats
# 47.42%
# of users with Python3
# Memory
# 16.48
# MB
# Beats
# 87.62%
# of users with Python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        @cache
        def impl(s1):
            n = len(s1)
            if not n:
                return [""]
            result = []
            c = ""
            for i in range(n):
                c += s1[i]
                if c in wordDict:
                    r = impl(s1[i+1:])
                    for ri in r:
                        r1 = c
                        if ri:
                            r1 += " " + ri
                        result.append(r1)
            return result

        return impl(s)


tests = [
    ["catsanddog", ["cat","cats","and","sand","dog"], ["cats and dog","cat sand dog"]],
    ["pineapplepenapple", ["apple","pen","applepen","pine","pineapple"], ["pine apple pen apple","pineapple pen apple","pine applepen apple"]],
    ["catsandog", ["cats","dog","sand","and","cat"], []],
]

run_functional_tests(Solution().wordBreak, tests, custom_check=compareSets)
