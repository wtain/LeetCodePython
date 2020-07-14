"""
https://leetcode.com/problems/plus-one/
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
from typing import List

"""
Runtime: 44 ms, faster than 35.29% of Python3 online submissions for Plus One.
Memory Usage: 14.1 MB, less than 5.50% of Python3 online submissions for Plus One.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()

        n = len(digits)

        carry = 1
        i = 0
        while carry > 0 and i < n:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i += 1

        if carry > 0:
            digits.append(carry)

        digits.reverse()
        return digits


print(Solution().plusOne([]))  # 1
print(Solution().plusOne([9]))  # 1 0
print(Solution().plusOne([9, 9]))  # 1 0 0
print(Solution().plusOne([1,2,3]))  # 1 2 4
print(Solution().plusOne([4,3,2,1]))  # 4 3 2 2