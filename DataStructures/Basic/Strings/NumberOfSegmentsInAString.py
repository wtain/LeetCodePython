"""
https://leetcode.com/problems/number-of-segments-in-a-string/
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 32 ms, faster than 56.91% of Python3 online submissions for Number of Segments in a Strings.
Memory Usage: 13.8 MB, less than 40.74% of Python3 online submissions for Number of Segments in a Strings.
"""
class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        n = len(s)
        i = 0
        while i < n:
            if not str.isspace(s[i]):
                cnt += 1
                while i < n and not str.isspace(s[i]):
                    i += 1
            i += 1

        return cnt


tests = [
    ["Hello, my name is John", 5]
]

run_functional_tests(Solution().countSegments, tests)
