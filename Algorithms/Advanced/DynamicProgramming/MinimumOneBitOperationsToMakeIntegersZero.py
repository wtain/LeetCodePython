"""
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2023-11-30

Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.



Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.


Constraints:

0 <= n <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 40
# ms
# Beats
# 59.09%
# of users with Python3
# Memory
# 16.28
# MB
# Beats
# 53.90%
# of users with Python3
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/editorial/?envType=daily-question&envId=2023-11-30
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         if n == 0:
#             return 0
#
#         k = 0
#         curr = 1
#         while curr * 2 <= n:
#             curr *= 2
#             k += 1
#         return 2 ** (k+1) - 1 - self.minimumOneBitOperations(n ^ curr)



# Runtime
# 33
# ms
# Beats
# 90.91%
# of users with Python3
# Memory
# 16.18
# MB
# Beats
# 78.57%
# of users with Python3
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/editorial/?envType=daily-question&envId=2023-11-30
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         result = 0
#         k = 0
#         mask = 1
#
#         while mask <= n:
#             if n & mask:
#                 result = 2 ** (k+1) - 1 - result
#
#             mask <<= 1
#             k += 1
#         return result


# Runtime
# 36
# ms
# Beats
# 83.77%
# of users with Python3
# Memory
# 16.20
# MB
# Beats
# 78.57%
# of users with Python3
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/editorial/?envType=daily-question&envId=2023-11-30
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        result = n
        result ^= result >> 16
        result ^= result >>  8
        result ^= result >>  4
        result ^= result >>  2
        result ^= result >>  1
        return result


tests = [
    [3, 2],
    [6, 4],
]

run_functional_tests(Solution().minimumOneBitOperations, tests)
