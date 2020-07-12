"""
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


# Runtime: 48 ms, faster than 6.09% of Python online submissions for Reverse Integer.
# Memory Usage: 12.8 MB, less than 28.76% of Python online submissions for Reverse Integer.
class Solution(object):

    def reversePositive(self, x):
        result = 0
        while x > 0:
            result = 10 * result + x % 10
            x //= 10
        if result < -2147483648 or result > 2147483647:
            return 0
        return result

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= -2147483648 or x > 2147483647:
            return 0
        if x < 0:
            return -self.reversePositive(-x)
        else:
            return self.reversePositive(x)


print(Solution().reverse(123))  # 321
print(Solution().reverse(-123))  # -321
print(Solution().reverse(120))  # 21
print(Solution().reverse(-2147483648))  # 0
print(Solution().reverse(1534236469))  # 0