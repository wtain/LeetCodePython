"""
https://leetcode.com/problems/isomorphic-strings/
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""
from typing import Dict, Set

"""
Runtime: 36 ms, faster than 89.43% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 14.2 MB, less than 21.19% of Python3 online submissions for Isomorphic Strings.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if len(t) != n:
            return False
        map: Dict[chr, chr] = {}
        other: Set[chr] = set()

        for i in range(0, n):
            if s[i] in map:
                if t[i] != map[s[i]]:
                    return False
            else:
                if t[i] in other:
                    return False
                map[s[i]] = t[i]
                other.add(t[i])
        return True


print(Solution().isIsomorphic("ab", "aa"))  # False
print(Solution().isIsomorphic("egg", "add"))  # True
print(Solution().isIsomorphic("foo", "bar"))  # False
print(Solution().isIsomorphic("paper", "title"))  # True

