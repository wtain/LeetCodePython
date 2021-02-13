"""
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1
"""


"""
Runtime: 28 ms, faster than 81.90% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 14 MB, less than 13.82% of Python3 online submissions for Valid Perfect Square.
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        d = 2
        dprev = 0
        while abs(d - dprev) > 1:
            v = (d + num / d) // 2
            dprev = d
            d = v
        return d**2 == num


print(Solution().isPerfectSquare(16))  # True
print(Solution().isPerfectSquare(14))  # False
