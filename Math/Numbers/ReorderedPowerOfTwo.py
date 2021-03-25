"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/
https://leetcode.com/problems/reordered-power-of-2/

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
"""
from typing import Set, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 81.85% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 14.2 MB, less than 52.82% of Python3 online submissions for Reordered Power of 2.
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:

        def get_digits(x: int) -> Dict[int, int]:
            result = dict()
            while x:
                d = x % 10
                result[d] = result.get(d, 0) + 1
                x //= 10
            return result

        N_digits = get_digits(N)

        for i in range(30):
            p = 1 << i
            p_digits = get_digits(p)
            if p_digits == N_digits:
                return True

        return False


tests = [
    (1521, False),

    (1, True),
    (10, False),
    (16, True),
    (46, True)
]

run_functional_tests(Solution().reorderedPowerOf2, tests)