"""
https://leetcode.com/problems/factorial-trailing-zeroes/

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""

# WRONG
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        n2 = 0
        n5 = 0
        for i in range(1, n+1):
            if 0 == i % 2:
                n2 += 1
            if 0 == i % 5:
                n5 += 1
        return min(n2, n5)
"""

"""
Runtime: 32 ms, faster than 59.98% of Python3 online submissions for Factorial Trailing Zeroes.
Memory Usage: 14 MB, less than 11.40% of Python3 online submissions for Factorial Trailing Zeroes.
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        n5 = 0
        while n > 0:
            n //= 5
            n5 += n
        return n5


print(Solution().trailingZeroes(3))  # 0
print(Solution().trailingZeroes(5))  # 1
print(Solution().trailingZeroes(500))  # 124

