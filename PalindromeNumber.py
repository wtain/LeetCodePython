"""
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""

"""
Runtime: 108 ms, faster than 12.05% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.7 MB, less than 93.31% of Python3 online submissions for Palindrome Number.
"""
class Solution:

    def getPowerOfTen(self, x: int) -> int:
        p = 1
        while x // p >= 10 or x // p <= -10:
            p *= 10
        return p

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = self.getPowerOfTen(x)
        r = 1
        xl = x
        xr = x
        while l > r:
            dl = xl // l
            xl %= l

            dr = xr % 10
            xr //= 10

            if dl != dr:
                return False

            l //= 10
            r *= 10
        return True


print(Solution().isPalindrome(1001))  # True
print(Solution().isPalindrome(121))  # True
print(Solution().isPalindrome(-121))  # False
print(Solution().isPalindrome(10))  # False