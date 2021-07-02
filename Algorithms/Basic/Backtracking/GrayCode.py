"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3799/
https://leetcode.com/problems/gray-code/

An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.



Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
Example 2:

Input: n = 1
Output: [0,1]


Constraints:

1 <= n <= 16
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 164 ms, faster than 20.70% of Python3 online submissions for Gray Code.
# Memory Usage: 21.7 MB, less than 56.11% of Python3 online submissions for Gray Code.
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#
#         def change_bit(v: int, i: int) -> int:
#             mask = 1 << i
#             return v ^ mask
#
#         result = []
#         v, used = 0, set()
#         used.add(0)
#         while not result or v:
#             result.append(v)
#             v1 = 0
#             for i in range(n):
#                 v1 = change_bit(v, i)
#                 if v1 not in used:
#                     used.add(v1)
#                     break
#             v = v1
#         return result



# Runtime: 108 ms, faster than 73.53% of Python3 online submissions for Gray Code.
# Memory Usage: 21.8 MB, less than 27.15% of Python3 online submissions for Gray Code.
# https://leetcode.com/problems/gray-code/solution/
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         def getGrayCodeHelper(n: int, result: List[int]):
#             if n == 0:
#                 result.append(0)
#                 return
#             getGrayCodeHelper(n-1, result)
#             m = len(result)
#             mask = 1 << (n-1)
#             for i in range(m-1, -1, -1):
#                 result.append(result[i] ^ mask)
#
#         result = []
#         getGrayCodeHelper(n, result)
#         return result


# Runtime: 104 ms, faster than 83.14% of Python3 online submissions for Gray Code.
# Memory Usage: 21.8 MB, less than 39.93% of Python3 online submissions for Gray Code.
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         result = [0]
#         for j in range(n):
#             m = len(result)
#             mask = 1 << j
#             for i in range(m - 1, -1, -1):
#                 result.append(result[i] ^ mask)
#         return result


# Runtime: 136 ms, faster than 34.84% of Python3 online submissions for Gray Code.
# Memory Usage: 21.8 MB, less than 27.15% of Python3 online submissions for Gray Code.
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         next_num = 0
#         def grayCodeHelper(result: List[int], n: int):
#             nonlocal next_num
#             if n == 0:
#                 result.append(next_num)
#                 return
#             grayCodeHelper(result, n-1)
#             next_num ^= 1 << (n-1)
#             grayCodeHelper(result, n - 1)
#
#         result = []
#         grayCodeHelper(result, n)
#         return result


# Runtime: 108 ms, faster than 73.53% of Python3 online submissions for Gray Code.
# Memory Usage: 21.7 MB, less than 56.11% of Python3 online submissions for Gray Code.
# class Solution:
#     def grayCode(self, n: int) -> List[int]:
#         m = 1 << n
#         result = []
#         for i in range(m):
#             result.append(i ^ (i >> 1))
#         return result


# Runtime: 100 ms, faster than 91.29% of Python3 online submissions for Gray Code.
# Memory Usage: 21.8 MB, less than 27.15% of Python3 online submissions for Gray Code.
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]


tests = [
    [2, [0,1,3,2]],
    [1, [0,1]]
]

run_functional_tests(Solution().grayCode, tests)