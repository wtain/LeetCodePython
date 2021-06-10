"""
https://leetcode.com/problems/thousand-separator/

Given an integer n, add a dot (".") as the thousands separator and return it in string format.



Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"


Constraints:

0 <= n < 2^31
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 93.90% of Python3 online submissions for Thousand Separator.
# Memory Usage: 14.2 MB, less than 70.60% of Python3 online submissions for Thousand Separator.
class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = []
        p = 0
        for c in reversed(str(n)):
            result.append(c)
            p += 1
            if p == 3:
                result.append('.')
                p = 0
        if result[-1] == '.':
            result.pop()
        return "".join(reversed(result))


tests = [
    [987, "987"],
    [1234, "1.234"],
    [123456789, "123.456.789"],
    [0, "0"]
]

run_functional_tests(Solution().thousandSeparator, tests, input_metric=lambda test: 1)