"""
https://leetcode.com/problems/repeated-substring-pattern/
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
from typing import List


"""
Runtime: 140 ms, faster than 39.71% of Python3 online submissions for Repeated Substring Pattern.
Memory Usage: 14.1 MB, less than 9.59% of Python3 online submissions for Repeated Substring Pattern.
"""
class Solution:

    def calcPrefixFunction(self, s: str) -> List[int]:
        n = len(s)
        p = [0] * n
        k = 0
        for i in range(1, n):
            while k > 0 and s[k] != s[i]:
                k = p[k-1]
            if s[k] == s[i]:
                k += 1
            p[i] = k
        return p

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False
        p = self.calcPrefixFunction(s)
        l = n - p[n-1]
        if n == l or n % l > 0:
            return False
        t = s[0:l]
        for i in range(0, n - l, l):
            si = s[i:i+l]
            if si != t:
                return False
        return True


print(Solution().repeatedSubstringPattern("abab"))  # True
print(Solution().repeatedSubstringPattern("aba"))  # False
print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
