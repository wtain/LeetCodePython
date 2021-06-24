"""
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.



Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true


Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 94.77% of Python3 online submissions for Check if Binary String Has at Most One Segment of Ones.
# Memory Usage: 14.1 MB, less than 90.31% of Python3 online submissions for Check if Binary String Has at Most One Segment of Ones.
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found, inside = False, False
        for c in s:
            if c == '1':
                if found and not inside:
                    return False
                found = True
                inside = True
            else:
                if found:
                    inside = False
        return True


tests = [
    ["1001", False],
    ["110", True]
]

run_functional_tests(Solution().checkOnesSegment, tests)