"""
https://leetcode.com/problems/add-two-integers/

Given two integers num1 and num2, return the sum of the two integers.


Example 1:

Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
Example 2:

Input: num1 = -10, num2 = 4
Output: -6
Explanation: num1 + num2 = -6, so -6 is returned.


Constraints:

-100 <= num1, num2 <= 100
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 41 ms, faster than 44.03% of Python3 online submissions for Add Two Integers.
# Memory Usage: 13.9 MB, less than 51.86% of Python3 online submissions for Add Two Integers.
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


tests = [
    [12, 5, 17],
    [-10, 4, -6]
]

run_functional_tests(Solution().sum, tests)
