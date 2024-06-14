"""
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def minIncrementForUnique(self, A: List[int]) -> int:
#         seen = set()
#         result = 0
#         for a in A:
#             while a in seen:
#                 a += 1
#                 result += 1
#             seen.add(a)
#         return result

# class Solution:
#     def minIncrementForUnique(self, A: List[int]) -> int:
#         result = 0
#
#         c = Counter(A)
#         keys = sorted(c.keys())
#         n = len(keys)
#         dups = 0
#         for i in range(n+1):
#             dups += (c[keys[i]] -1) if i < n else 0
#             space = ((keys[i] - keys[i-1]-1) if i < n else len(A)) if i > 0 else 0
#             could_allocate = min(space, dups)
#             result += (1 + dups) * dups // 2
#             dups -= could_allocate
#
#         return result

# Runtime: 1172 ms, faster than 12.95% of Python3 online submissions for Minimum Increment to Make Array Unique.
# Memory Usage: 21.3 MB, less than 27.48% of Python3 online submissions for Minimum Increment to Make Array Unique.
# class Solution:
#     def minIncrementForUnique(self, A: List[int]) -> int:
#         result = 0
#
#         c = Counter(A)
#
#         taken = []
#         for x in range(100000):
#             if c[x] >= 2:
#                 taken.extend([x] * (c[x] - 1))
#             elif taken and c[x] == 0:
#                 result += x - taken.pop()
#
#         return result

# WRONG
# Runtime: 340 ms, faster than 52.52% of Python3 online submissions for Minimum Increment to Make Array Unique.
# Memory Usage: 19.5 MB, less than 78.56% of Python3 online submissions for Minimum Increment to Make Array Unique.
# class Solution:
#     def minIncrementForUnique(self, A: List[int]) -> int:
#         result = 0
#
#         taken = 0
#         A.sort()
#         A.append(100000)
#         for i in range(1, len(A)):
#             if A[i] == A[i-1]:
#                 taken += 1
#                 result -= A[i]
#             else:
#                 give = min(taken, A[i] - A[i-1] - 1)
#                 result += give * (give+1) // 2 + give * A[i-1]
#                 taken -= give
#         return result


# Runtime
# 573
# ms
# Beats
# 93.24%
# Analyze Complexity
# Memory
# 30.17
# MB
# Beats
# 89.64%
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/editorial/?envType=daily-question&envId=2024-06-14
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        n = len(A)
        max_val = max(A)
        result = 0

        freq_cnt = [0] * (n + max_val + 1)

        for val in A:
            freq_cnt[val] += 1

        for i in range(len(freq_cnt)):
            if freq_cnt[i] <= 1:
                continue

            duplicates = freq_cnt[i] - 1
            freq_cnt[i+1] += duplicates
            freq_cnt[i] = 1
            result += duplicates

        return result


tests = [
    [[1,2,2], 1],
    [[3,2,1,2,1,7], 6],
]

run_functional_tests(Solution().minIncrementForUnique, tests)
