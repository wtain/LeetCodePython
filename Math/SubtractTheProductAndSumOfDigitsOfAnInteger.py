"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21


Constraints:

1 <= n <= 10^5

Runtime: 76 ms, faster than 5.85% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
Memory Usage: 14.3 MB, less than 5.15% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        dsum = 0
        while n > 0:
            digit = n % 10
            n = int(n / 10)
            dsum += digit
            prod *= digit
        return prod - dsum


print(Solution().subtractProductAndSum(234))  # 15
print(Solution().subtractProductAndSum(4421))  # 21
