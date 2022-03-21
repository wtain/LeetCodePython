"""
https://leetcode.com/problems/a-number-after-a-double-reversal/

Reversing an integer means to reverse all its digits.

For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.



Example 1:

Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
Example 2:

Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
Example 3:

Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.


Constraints:

0 <= num <= 106
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 26.15% of Python3 online submissions for A Number After a Double Reversal.
# Memory Usage: 13.8 MB, less than 64.26% of Python3 online submissions for A Number After a Double Reversal.
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if not num:
            return True
        return num % 10


tests = [
    [526, True],
    [1800, False],
    [0, True]
]

run_functional_tests(Solution().isSameAfterReversals, tests)
