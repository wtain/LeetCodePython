"""
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
Example 2:

Input: n = 11
Output: [2,9]
Example 3:

Input: n = 10000
Output: [1,9999]
Example 4:

Input: n = 69
Output: [1,68]
Example 5:

Input: n = 1010
Output: [11,999]


Constraints:

2 <= n <= 10^4
"""
from typing import List


# WRONG
# class Solution:
#     def getNoZeroIntegers(self, n: int) -> List[int]:
#         a = 0
#         b = 0
#         e = 10 ** 4
#         c = 0
#         while n or c:
#             if not e:
#                 e = 1
#             di = n // e + c
#             n %= e
#             e //= 10
#             if not di:
#                 continue
#             if di > 1:
#                 a = 10*a + di-1 + c // 10
#                 b = 10*b + 1
#                 c = 0
#             else:
#                 c = 10
#
#         return [a, b]

# Runtime: 28 ms, faster than 86.03% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
# Memory Usage: 14.3 MB, less than 9.31% of Python3 online submissions for Convert Integer to the Sum of Two No-Zero Integers.
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def hasZeros(x: int) -> bool:
            while x:
                if not x % 10:
                    return True
                x //= 10
            return False

        for i in range(1, n+1):
            x = n-i
            if not hasZeros(i) and not hasZeros(x):
                return [i, x]
        return []


tests = [
    (2, [1,1]),
    (11, [2,9]),
    (10000, [1,9999]),
    (69, [1,68]),
    (1010, [11,999])
]

for test in tests:
    result = Solution().getNoZeroIntegers(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))