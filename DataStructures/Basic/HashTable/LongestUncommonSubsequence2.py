"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3921/
https://leetcode.com/problems/longest-uncommon-subsequence-ii/

Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3
Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1


Constraints:

1 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] consists of lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 85.26% of Python3 online submissions for Longest Uncommon Subsequence II.
# Memory Usage: 14.4 MB, less than 39.74% of Python3 online submissions for Longest Uncommon Subsequence II.
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/1428753/Python-O(n2k)-solution-explained
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            t = iter(t)
            return all(c in t for c in s)

        strs.sort(key=lambda s: -len(s))
        for i, s in enumerate(strs):
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)
        return -1


tests = [
    [["aabbcc", "aabbcc","cb"], 2],
    [["aba","cdc","eae"], 3],
    [["aaa","aaa","aa"], -1]
]

run_functional_tests(Solution().findLUSlength, tests)