"""
https://leetcode.com/problems/longest-palindrome/
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from typing import Dict


"""
Runtime: 32 ms, faster than 75.06% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.8 MB, less than 76.17% of Python3 online submissions for Longest Palindrome.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        let: Dict[chr, int] = {}
        for c in s:
            let[c] = (let.get(c) or 0) + 1
        hasOdd = False
        result = 0
        for l in let:
            cnt = let[l]
            result += 2 * (cnt // 2)
            if not hasOdd and cnt % 2 == 1:
                hasOdd = True
                result += 1
        return result


print(Solution().longestPalindrome("abccccdd"))  # 7
