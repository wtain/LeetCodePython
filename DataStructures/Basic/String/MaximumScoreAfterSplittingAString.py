"""
https://leetcode.com/problems/maximum-score-after-splitting-a-string/

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.



Example 1:

Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3


Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 82.95% of Python3 online submissions for Maximum Score After Splitting a String.
# Memory Usage: 14.1 MB, less than 73.40% of Python3 online submissions for Maximum Score After Splitting a String.
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        s0 = 0
        s1 = sum(1 for c in s if c == '1')
        n = len(s)
        for i in range(n-1):
            if s[i] == '0':
                s0 += 1
            else:
                s1 -= 1
            max_score = max(max_score, s0 + s1)
        return max_score


tests = [
    ["011101", 5],
    ["00111", 5],
    ["1111", 3]
]

run_functional_tests(Solution().maxScore, tests)