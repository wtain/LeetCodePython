"""
https://leetcode.com/problems/substring-with-largest-variance/description/

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 8172 ms
# Beats
# 19.66%
# Memory
# 16.5 MB
# Beats
# 25.64%
# https://leetcode.com/problems/substring-with-largest-variance/editorial/
class Solution:
    def largestVariance(self, s: str) -> int:
        cnt = Counter(s)
        result = 0
        for ci in cnt.keys():
            for cj in cnt.keys():
                if ci == cj:
                    continue
                icnt, jcnt = 0, 0
                rest_j = cnt[cj]

                for c in s:
                    if c == ci:
                        icnt += 1
                    if c == cj:
                        jcnt += 1
                        rest_j -= 1
                    if jcnt > 0:
                        result = max(result, icnt -jcnt)
                    if icnt < jcnt and rest_j > 0:
                        icnt, jcnt = 0, 0
        return result


tests = [
    ["aababbb", 3],
    ["abcde", 0],
]

run_functional_tests(Solution().largestVariance, tests)
