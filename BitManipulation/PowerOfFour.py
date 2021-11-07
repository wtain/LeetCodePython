"""
https://leetcode.com/problems/power-of-four/
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 60 ms, faster than 5.53% of Python3 online submissions for Power of Four.
Memory Usage: 14 MB, less than 17.47% of Python3 online submissions for Power of Four.
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and num & 0xAAAAAAAAAAAAAAAA == 0


tests = [
    [16, True],
    [5, False]
]

run_functional_tests(Solution().isPowerOfFour, tests)
