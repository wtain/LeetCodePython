"""
https://leetcode.com/problems/smallest-even-multiple/

Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.


Example 1:

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.


Constraints:

1 <= n <= 150
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 26 ms
# Beats
# 97.84%
# Memory
# 13.8 MB
# Beats
# 49.35%
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return 2 * n


tests = [
    [5, 10],
    [6, 6]
]

run_functional_tests(Solution().smallestEvenMultiple, tests)
