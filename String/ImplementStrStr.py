"""
https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""
from typing import List

"""
Runtime: 68 ms, faster than 7.70% of Python3 online submissions for Implement strStr().
Memory Usage: 14.9 MB, less than 5.02% of Python3 online submissions for Implement strStr().
"""
class Solution:

    def prefix(self, s: str) -> List[int]:
        n = len(s)
        p = [0] * n
        for i in range(1, n):
            k = p[i-1]
            while k > 0 and s[k] != s[i]:
                k = p[k - 1]
            if s[k] == s[i]:
                k += 1
            p[i] = k
        return p


    def strStr(self, haystack: str, needle: str) -> int:
        k = 0
        m = len(needle)
        if m == 0:
            return 0
        p = self.prefix(needle)
        for i in range(len(haystack)):
            while k > 0 and haystack[i] != needle[k]:
                k = p[k-1]
            if haystack[i] == needle[k]:
                k += 1
            if k == m:
                return i-m+1
        return -1


print(Solution().strStr("hello", "ll"))  # 2
print(Solution().strStr("aaaaa", "bba"))  # -1
print(Solution().strStr("aaaaa", ""))  # 0
print(Solution().strStr("bbbaaaaa", "bba"))  # 1
print(Solution().strStr("bbbabababbaa", "babba"))  # 6
