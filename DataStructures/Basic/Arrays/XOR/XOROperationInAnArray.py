"""
https://leetcode.com/problems/xor-operation-in-an-array/

Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.



Example 1:

Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
Example 2:

Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
Example 3:

Input: n = 1, start = 7
Output: 7
Example 4:

Input: n = 10, start = 5
Output: 2


Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length
"""

# Runtime: 32 ms, faster than 61.06% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 14.2 MB, less than 53.94% of Python3 online submissions for XOR Operation in an Array.
# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         result = 0
#         for i in range(n):
#             result ^= start + 2 * i
#         return result

# Runtime: 28 ms, faster than 84.74% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 13.8 MB, less than 99.97% of Python3 online submissions for XOR Operation in an Array.
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 1
        result = start
        start += 2 * i
        for i in range(1, n):
            result ^= start
            start += 2
        return result


tests = [
    (5, 0, 8),
    (4, 3, 8),
    (1, 7, 7),
    (10, 5, 2)
]

for test in tests:
    result = Solution().xorOperation(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))