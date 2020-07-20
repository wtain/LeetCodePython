"""
https://leetcode.com/problems/power-of-two/
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
"""

"""
Runtime: 32 ms, faster than 79.29% of Python3 online submissions for Power of Two.
Memory Usage: 14 MB, less than 10.69% of Python3 online submissions for Power of Two.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


print(Solution().isPowerOfTwo(0))  # False
print(Solution().isPowerOfTwo(1))  # True
print(Solution().isPowerOfTwo(16))  # True
print(Solution().isPowerOfTwo(218))  # False
