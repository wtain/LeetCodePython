"""
https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
"""



"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1
            a ^= b
            b = carry
        return a
"""

"""
Runtime: 28 ms, faster than 77.38% of Python3 online submissions for Sum of Two Integers.
Memory Usage: 13.9 MB, less than 21.55% of Python3 online submissions for Sum of Two Integers.
"""
class Solution:

    def addOne(self, a: int) -> int:
        c = 1
        while c > 0:
            c1 = c & a
            a ^= c
            c = c1 << 1
        return a

    def negate(self, a: int) -> int:
        return self.addOne(~a)

    def getSum(self, a: int, b: int) -> int:
        if a < 0 and b < 0:
            return self.negate(self.getSum(self.negate(a), self.negate(b)))
        result = 0
        mask = 1
        carry = 0
        for i in range(32):
            ai = a & mask
            bi = b & mask
            result |= (ai ^ bi ^ carry)
            carry = (ai & bi | ai & carry | bi & carry) << 1
            mask <<= 1
        if result == 0xFFFFFFFF:
            return self.negate(1)
        return result


print(Solution().getSum(2147483647, -2147483648))  # -1
print(Solution().getSum(-12, -8))  # -20
print(Solution().getSum(1, 2))  # 3
print(Solution().getSum(-2, 3))  # 1

