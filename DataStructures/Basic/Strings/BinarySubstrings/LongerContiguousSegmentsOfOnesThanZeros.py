"""
https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/

Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.



Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.


Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 16 ms, faster than 99.95% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
# Memory Usage: 13.9 MB, less than 98.19% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        l0, l1 = 0, 0
        c0, c1 = 0, 0
        for c in s:
            if c == '0':
                c1 = 0
                c0 += 1
            else:
                c0 = 0
                c1 += 1
            l0 = max(l0, c0)
            l1 = max(l1, c1)
        return l1 > l0


tests = [
    ["1101", True],
    ["111000", False],
    ["110100010", False]
]

run_functional_tests(Solution().checkZeroOnes, tests)