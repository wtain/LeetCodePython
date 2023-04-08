"""
https://leetcode.com/problems/circular-permutation-in-binary-representation/

Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

p[0] = start
p[i] and p[i+1] differ by only one bit in their binary representation.
p[0] and p[2^n -1] must also differ by only one bit in their binary representation.


Example 1:

Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01).
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
Example 2:

Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).


Constraints:

1 <= n <= 16
0 <= start < 2 ^ n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def circularPermutation(self, n: int, start: int) -> List[int]:
#         result = [start]
#         m = 1 << n
#         i, j = 0, 1
#         for k in range(1, m):
#             value = result[-1]
#             if i < j:
#                 value ^= value & (1 << i)
#                 i += 1
#             else:
#                 value ^= value & (1 << j)
#                 j += 1
#                 j %= n
#                 i = 0
#
#             result.append(value)
#         return result

# return [i ^ (i >> 1) for i in map(lambda i: (n-1-start+i) % (1 << n), range(1 << n))]


# Runtime
# 196 ms
# Beats
# 60.32%
# Memory
# 22.2 MB
# Beats
# 87.30%
# class Solution:
#     def circularPermutation(self, n: int, start: int) -> List[int]:
#         graycode = [i ^ (i >> 1) for i in range(1 << n)]
#         i = graycode.index(start)
#         return graycode[i:] + graycode[:i]


# Runtime
# 183 ms
# Beats
# 88.89%
# Memory
# 22.3 MB
# Beats
# 77.78%
# https://leetcode.com/problems/circular-permutation-in-binary-representation/solutions/414203/java-c-python-4-line-gray-code/
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]


"""
11
10
00
01

010
110
111
101
100
000
001
011


11
10
00
01


 a0  a1 ...  a(n-3)  a(n-2)  a(n-1)
 a0  a1 ...  a(n-3)  a(n-2) !a(n-1)
 a0  a1 ...  a(n-3) !a(n-2) !a(n-1)
 a0  a1 ...  a(n-3) !a(n-2)  a(n-1)
 a0  a1 ... !a(n-3) !a(n-2)  a(n-1)
 a0  a1 ... !a(n-3) !a(n-2) !a(n-1)
 a0  a1 ... !a(n-3)  a(n-2)  a(n-1)
 a0  a1 ... !a(n-3)  a(n-2) !a(n-1)


"""

def customCheck(test, result):
    n = test[0]
    start = test[1]
    m = 1 << n

    def isPowerOfTwo(n: int) -> bool:
        return n > 0 and n & (n-1) == 0

    if len(result) != m:
        return False
    if list(sorted(result)) != list(range(m)):
        return False
    if result[0] != start:
        return False
    for i in range(m):
        j = (i+m-1) % m
        diff = result[i] ^ result[j]
        if not isPowerOfTwo(diff):
            return False
    return True


tests = [
    [2, 3, [3,2,0,1]],
    [3, 2, [2,6,7,5,4,0,1,3]],
]

run_functional_tests(Solution().circularPermutation, tests, custom_check=customCheck)
