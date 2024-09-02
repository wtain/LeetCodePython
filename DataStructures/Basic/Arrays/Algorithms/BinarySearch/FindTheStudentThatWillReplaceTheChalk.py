"""
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02

There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

Return the index of the student that will replace the chalk pieces.



Example 1:

Input: chalk = [5,1,5], k = 22
Output: 0
Explanation: The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.
Student number 0 does not have enough chalk, so they will have to replace it.
Example 2:

Input: chalk = [3,4,1,2], k = 25
Output: 1
Explanation: The students go in turns as follows:
- Student number 0 uses 3 chalk so k = 22.
- Student number 1 uses 4 chalk so k = 18.
- Student number 2 uses 1 chalk so k = 17.
- Student number 3 uses 2 chalk so k = 15.
- Student number 0 uses 3 chalk so k = 12.
- Student number 1 uses 4 chalk so k = 8.
- Student number 2 uses 1 chalk so k = 7.
- Student number 3 uses 2 chalk so k = 5.
- Student number 0 uses 3 chalk so k = 2.
Student number 1 does not have enough chalk, so they will have to replace it.


Constraints:

chalk.length == n
1 <= n <= 105
1 <= chalk[i] <= 105
1 <= k <= 109
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         i = 0
#         n = len(chalk)
#         while k:
#             if k < chalk[i]:
#                 return i
#             k -= chalk[i]
#             i += 1
#             i %= n
#         return 0


# Runtime
# 563
# ms
# Beats
# 88.52%
# Analyze Complexity
# Memory
# 30.60
# MB
# Beats
# 19.92%
# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         i = 0
#         n = len(chalk)
#         s = sum(chalk)
#         k %= s
#         while True:
#             if k < chalk[i]:
#                 return i
#             k -= chalk[i]
#             i += 1
#             i %= n


# Runtime
# 579
# ms
# Beats
# 48.81%
# Analyze Complexity
# Memory
# 30.66
# MB
# Beats
# 19.92%
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/editorial/?envType=daily-question&envId=2024-09-02
# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         s = 0
#         n = len(chalk)
#         for i in range(n):
#             s += chalk[i]
#             if k < s:
#                 break
#         k %= s
#         for i in range(n):
#             if k < chalk[i]:
#                 return i
#             k -= chalk[i]
#         return 0


# Runtime
# 617
# ms
# Beats
# 5.94%
# Analyze Complexity
# Memory
# 30.10
# MB
# Beats
# 62.80%
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/editorial/?envType=daily-question&envId=2024-09-02
# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         n = len(chalk)
#         prefix_sum = [0] * n
#         prefix_sum[0] = chalk[0]
#         for i in range(1, n):
#             prefix_sum[i] = prefix_sum[i-1] + chalk[i]
#
#         sum_chalk = prefix_sum[-1]
#         remaining_chalk = k % sum_chalk
#
#         def binsearch(arr, tar):
#             low, high = 0, len(arr)-1
#             while low < high:
#                 mid = low + (high - low) // 2
#                 if arr[mid] <= tar:
#                     low = mid + 1
#                 else:
#                     high = mid
#             return high
#
#         return binsearch(prefix_sum, remaining_chalk)


# Runtime
# 613
# ms
# Beats
# 6.99%
# Analyze Complexity
# Memory
# 29.99
# MB
# Beats
# 68.60%
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + chalk[i]

        sum_chalk = prefix_sum[-1]
        remaining_chalk = k % sum_chalk

        return bisect.bisect_right(prefix_sum, remaining_chalk)


tests = [
    [[5,1,5], 22, 0],
    [[3,4,1,2], 25, 1],
    [[73,79,31,60,84,46,91,27,27,58,16,1,3,43,54,92,84,76,39,27,87,68,5,42,10,90,78,24,95,83,52,73,70,82,22,63,22,23,68,98,4,56,68,50,22,10,9,87,64,37,28,18,14,75,32,53,19,78,83,72,26,94,14,80,66,81,50,18,97,9,21,51,40,12,25,62,47,20,60,43,73,82,91,87,44,29,10,15,99,51,35,54,78,30,69,68,13,32,7,39,87,66,90,60,3,67,68,82,37], 375647757, 102],
    [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 999999999, 999],
]

run_functional_tests(Solution().chalkReplacer, tests)
