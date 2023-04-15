"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.



Example 1:

example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
Example 2:

Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.
Example 3:

Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.


Constraints:

2 <= s.length <= 12
s consists of lowercase English letters only.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 426 ms
# Beats
# 97.79%
# Memory
# 14 MB
# Beats
# 86.49%
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/solutions/1458289/mask-dp/
class Solution:
    def maxProduct(self, s: str) -> int:
        dp = [0] * (1 << 12)

        def palindrome_size(mask):
            p1, p2 = 0, len(s)
            result = 0
            while p1 <= p2:
                if mask & (1 << p1) == 0:
                    p1 += 1
                elif mask & (1 << p2) == 0:
                    p2 -= 1
                elif s[p1] != s[p2]:
                    return 0
                else:
                    result += 1 + (1 if p1 != p2 else 0)
                    p1 += 1
                    p2 -= 1
            return result

        result, mask = 0, (1 << len(s)) - 1
        for m in range(1, mask+1):
            dp[m] = palindrome_size(m)

        for m1 in range(mask, -1, -1):
            if dp[m1] * (len(s) - dp[m1]) > result:
                m2 = mask ^ m1
                while m2 > 0:
                    result = max(result, dp[m1] * dp[m2])
                    m2 = (m2-1) & (mask ^ m1)
        return result


tests = [
    ["leetcodecom", 9],
    ["bb", 1],
    ["accbcaxxcxx", 25],
]

run_functional_tests(Solution().maxProduct, tests)
