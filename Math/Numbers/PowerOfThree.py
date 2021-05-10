"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3722/
https://leetcode.com/problems/power-of-three/
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""


# Runtime: 68 ms, faster than 86.65% of Python3 online submissions for Power of Three.
# Memory Usage: 14.2 MB, less than 47.05% of Python3 online submissions for Power of Three.
"""
Runtime: 84 ms, faster than 64.35% of Python3 online submissions for Power of Three.
Memory Usage: 13.6 MB, less than 97.62% of Python3 online submissions for Power of Three.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 12157665459056928801 % n == 0


print(Solution().isPowerOfThree(-3))  # False
print(Solution().isPowerOfThree(27))  # True
print(Solution().isPowerOfThree(0))  # False
print(Solution().isPowerOfThree(9))  # True
print(Solution().isPowerOfThree(45))  # False
