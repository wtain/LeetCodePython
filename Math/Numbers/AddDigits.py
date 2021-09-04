"""
https://leetcode.com/problems/add-digits/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


"""
Runtime: 40 ms, faster than 30.28% of Python3 online submissions for Add Digits.
Memory Usage: 13.7 MB, less than 88.83% of Python3 online submissions for Add Digits.
"""
"""
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            num = sum
        return num
"""

"""
Runtime: 40 ms, faster than 30.28% of Python3 online submissions for Add Digits.
Memory Usage: 13.6 MB, less than 99.05% of Python3 online submissions for Add Digits.
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if 0 == num:
            return 0
        num %= 9
        if num == 0:
            num = 9
        return num


print(Solution().addDigits(0))  # 0
print(Solution().addDigits(38))  # 2
