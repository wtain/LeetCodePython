"""
https://leetcode.com/problems/find-the-pivot-integer/

Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.



Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.


Constraints:

1 <= n <= 1000
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 34 ms
# Beats
# 97.87%
# Memory
# 13.9 MB
# Beats
# 16.54%
class Solution:
    def pivotInteger(self, n: int) -> int:
        # S(1..x) = S(x..n)
        # S(0) = 0
        # (1+x) * x // 2 = S(n) - S(x-1)
        # 2 * S(x) - x = S(n)
        # (1+x) * x - x = (n+1)*n // 2
        # x^2=(n+1)*n // 2
        # (x-1)^2 = (n+1)*n // 2
        # x = sqrt((n+1)*n // 2)
        x = math.sqrt((n+1)*n / 2)
        return int(x) if x == int(x) else -1


tests = [
    [8, 6],
    [1, 1],
    [4, -1]
]

run_functional_tests(Solution().pivotInteger, tests)
