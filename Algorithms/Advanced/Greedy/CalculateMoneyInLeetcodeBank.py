"""
https://leetcode.com/problems/calculate-money-in-leetcode-bank/

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.



Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.


Constraints:

1 <= n <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 20 ms, faster than 99.45% of Python3 online submissions for Calculate Money in Leetcode Bank.
# Memory Usage: 14.2 MB, less than 39.61% of Python3 online submissions for Calculate Money in Leetcode Bank.
class Solution:
    def totalMoney(self, n: int) -> int:
        n_weeks = n // 7
        n_days = n % 7
        # week = (1 + 2 + .. + 7) + 7 * i = 28 + i * 7
        # S = (a1 + an) * n / 2 = (a1 + a1 + (n-1) * d) * n / 2 = a1*n + d * n * (n-1) / 2
        # sum_weeks = 28 + 28
        # first_day = 1 + num_weeks
        # sum_days = (first_day + first_day + (num_days-1)) * num_days / 2 =
        # first_day * num_days + num_days * (num_days - 1) / 2
        # (1 + n_weeks) * n_days + n_weeks * (n_days-1) * n_days // 2
        return 28 * n_weeks + 7 * n_weeks * (n_weeks-1) // 2 + \
               (1 + n_weeks) * n_days + (n_days-1) * n_days // 2


tests = [
    [4, 10],
    [10, 37],
    [20, 96]
]


run_functional_tests(Solution().totalMoney, tests)