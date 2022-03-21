"""
https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.



Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc.
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.


Constraints:

1000 <= num <= 9999
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 27.46% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
# Memory Usage: 13.8 MB, less than 97.03% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
class Solution:
    def minimumSum(self, num: int) -> int:
        d1 = num // 1000
        num %= 1000
        d2 = num // 100
        num %= 100
        d3 = num // 10
        d4 = num % 10
        digits = sorted([d1, d2, d3, d4])
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]


tests = [
    [2932, 52],
    [4009, 13]
]

run_functional_tests(Solution().minimumSum, tests)
