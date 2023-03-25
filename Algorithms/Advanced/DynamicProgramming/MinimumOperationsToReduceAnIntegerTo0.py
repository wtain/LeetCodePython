"""
https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.



Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
Example 2:

Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.


Constraints:

1 <= n <= 105
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minOperations(self, n: int) -> int:
#         dp = [math.inf] * (n+1)
#         dp[0] = 0
#         for i in range(1, n+1):
#             step = 1
#             while step <= i:
#                 j = i - step
#                 dp[i] = min(dp[i], dp[j]+1)
#                 step *= 2
#         return dp[n]


# Runtime
# 35 ms
# Beats
# 44.24%
# Memory
# 13.9 MB
# Beats
# 55.47%
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203994/java-c-python-1-line-solution/
# class Solution:
#     def minOperations(self, n: int) -> int:
#         result = 0
#         while n > 0:
#             if n & 1 == 0:
#                 n >>= 1
#             elif n & 2:
#                 n += 1
#                 result += 1
#             else:
#                 result += 1
#                 n >>= 2
#         return result

# Runtime
# 34 ms
# Beats
# 52.27%
# Memory
# 13.8 MB
# Beats
# 55.47%
# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/solutions/3203994/java-c-python-1-line-solution/
class Solution:
    def minOperations(self, n: int) -> int:
        return bin(n ^ (n*3)).count("1")


tests = [
    [39, 3],
    [54, 3],
]

run_functional_tests(Solution().minOperations, tests)
