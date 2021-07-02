"""
https://leetcode.com/problems/sum-of-digits-in-base-k/

Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.



Example 1:

Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
Example 2:

Input: n = 10, k = 10
Output: 1
Explanation: n is already in base 10. 1 + 0 = 1.


Constraints:

1 <= n <= 100
2 <= k <= 10
"""
from functools import reduce

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 20 ms, faster than 98.99% of Python3 online submissions for Sum of Digits in Base K.
# Memory Usage: 14.1 MB, less than 71.49% of Python3 online submissions for Sum of Digits in Base K.
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        while n:
            result += n % k
            n //= k
        return result


tests = [
    [34, 6, 9],
    [10, 10, 1]
]

run_functional_tests(Solution().sumBase, tests)