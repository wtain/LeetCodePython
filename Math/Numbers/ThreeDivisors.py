"""
https://leetcode.com/problems/three-divisors/

Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.



Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.
Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.


Constraints:

1 <= n <= 104
"""
from math import sqrt

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 84.83% of Python3 online submissions for Three Divisors.
# Memory Usage: 14.1 MB, less than 91.33% of Python3 online submissions for Three Divisors.
class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False

        def count_divisors(n: int) -> int:
            ns = int(sqrt(n))
            cnt = 2
            for k in range(2, ns+1):
                if n % k == 0:
                    if k ** 2 != n:
                        cnt += 2
                    else:
                        cnt += 1
            return cnt
        return count_divisors(n) == 3


tests = [
    [2, False],
    [4, True]
]

run_functional_tests(Solution().isThree, tests)