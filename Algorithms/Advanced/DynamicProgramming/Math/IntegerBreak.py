"""
https://leetcode.com/problems/integer-break/description/?envType=daily-question&envId=2023-10-06

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.



Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


Constraints:

2 <= n <= 58
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 36ms
# Beats 80.66%of users with Python3
# Memory
# Details
# 16.12MB
# Beats 85.57%of users with Python3
class Solution:
    def integerBreak(self, n: int) -> int:
        trivial = [0, 1, 1, 2, 4]
        if n < len(trivial):
            return trivial[n]
        r3 = n % 3
        if r3 == 0:
            return 3 ** (n // 3)
        elif r3 == 1:
            return 2 * 2 * 3 ** ((n-4) // 3)
        else:
            return 2 * 3 ** ((n-2) // 3)


tests = [
    [2, 1],
    [10, 36],
]

run_functional_tests(Solution().integerBreak, tests)
