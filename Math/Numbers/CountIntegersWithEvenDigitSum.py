"""
https://leetcode.com/problems/count-integers-with-even-digit-sum/

Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.



Example 1:

Input: num = 4
Output: 2
Explanation:
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.
Example 2:

Input: num = 30
Output: 14
Explanation:
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.


Constraints:

1 <= num <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 73 ms, faster than 34.42% of Python3 online submissions for Count Integers With Even Digit Sum.
# Memory Usage: 13.8 MB, less than 60.66% of Python3 online submissions for Count Integers With Even Digit Sum.
class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        for v in range(1, num+1):
            value = v
            s = 0
            while value:
                s += value % 10
                value //= 10
            if s % 2:
                continue
            cnt += 1
        return cnt


tests = [
    [4, 2],
    [30, 14]
]

run_functional_tests(Solution().countEven, tests)
