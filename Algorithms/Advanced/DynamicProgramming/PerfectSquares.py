"""
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


Constraints:

1 <= n <= 104
"""
import bisect
import math

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 96.71% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14.4 MB, less than 55.42% of Python3 online submissions for Perfect Squares.
class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return 0
        ns = int(math.sqrt(n) + 1)
        r = [0] * (ns + 1)
        for i_s in range(1, ns+1):
            is2 = i_s ** 2
            if is2 == n:
                return 1
            r[i_s] = is2
        for i in range(1, ns+1):
            t = n - r[i]
            j = bisect.bisect_left(r, t)
            if 0 <= j < len(r) and r[j] == t:
                return 2
        for i in range(1, ns+1):
            for j in range(1, ns+1):
                t = n - r[i] - r[j]
                k = bisect.bisect_left(r, t)
                if 0 <= k < len(r) and r[k] == t:
                    return 3
        return 4


tests = [
    [12, 3],
    [13, 2]
]

run_functional_tests(Solution().numSquares, tests)