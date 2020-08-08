"""
https://leetcode.com/problems/number-complement/
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.



Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Constraints:

The given integer num is guaranteed to fit within the range of a 32-bit signed integer.
num >= 1
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""


"""
Runtime: 68 ms, faster than 7.64% of Python3 online submissions for Number Complement.
Memory Usage: 13.9 MB, less than 36.53% of Python3 online submissions for Number Complement.
"""
class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        shift = 0
        while num > 0:
            di = 1 - num & 1
            result |= (di << shift)
            shift += 1
            num >>= 1
        return result
    # 5 = 101 -> 010
    # 1 = 1 -> 0


print(Solution().findComplement(5))  # 2
print(Solution().findComplement(1))  # 0
