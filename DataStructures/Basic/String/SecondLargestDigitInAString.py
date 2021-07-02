"""
https://leetcode.com/problems/second-largest-digit-in-a-string/

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.



Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.


Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 28 ms, faster than 97.50% of Python3 online submissions for Second Largest Digit in a String.
# Memory Usage: 14.2 MB, less than 77.31% of Python3 online submissions for Second Largest Digit in a String.
class Solution:
    def secondHighest(self, s: str) -> int:
        a, b = -1, -1
        for c in s:
            if str.isdigit(c):
                v = ord(c) - ord('0')
                if v > a:
                    b, a = a, v
                elif v != a and v > b:
                    b = v
        return b


tests = [
    ["dfa12321afd", 2],
    ["abc1111", -1]
]

run_functional_tests(Solution().secondHighest, tests)