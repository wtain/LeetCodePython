"""
https://leetcode.com/problems/frog-jump-ii/

You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.

A frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.

The length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.

More formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.
The cost of a path is the maximum length of a jump among all jumps in the path.

Return the minimum cost of a path for the frog.



Example 1:


Input: stones = [0,2,5,6,7]
Output: 5
Explanation: The above figure represents one of the optimal paths the frog can take.
The cost of this path is 5, which is the maximum length of a jump.
Since it is not possible to achieve a cost of less than 5, we return it.
Example 2:


Input: stones = [0,3,9]
Output: 9
Explanation:
The frog can jump directly to the last stone and come back to the first stone.
In this case, the length of each jump will be 9. The cost for the path will be max(9, 9) = 9.
It can be shown that this is the minimum achievable cost.


Constraints:

2 <= stones.length <= 105
0 <= stones[i] <= 109
stones[0] == 0
stones is sorted in a strictly increasing order.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxJump(self, stones: List[int]) -> int:
#         n = len(stones)
#
#         def can_jump(k: int) -> bool:
#             nonlocal n
#             available = set(stones)
#             i = 0
#             while i < n - 1:
#                 i0 = i
#                 while i+1 < n and stones[i+1] <= stones[i0] + k:
#                     i += 1
#                 if i == i0:
#                     return False
#                 if stones[i] > stones[i0] + k:
#                     return False
#                 available.remove(stones[i])
#             i = n - 1
#             while i > 0:
#                 i0 = i
#                 while i > 0 and stones[i-1] + k >= stones[i0] and stones[i-1] in available:
#                     i -= 1
#                 if i == i0:
#                     return False
#                 if stones[i] < stones[i0] - k:
#                     return False
#             return True
#
#         l, r = 1, stones[-1]
#         while l < r:
#             m = l + (r - l) // 2
#             if can_jump(m):
#                 r = m+1
#             else:
#                 l = m
#
#         return l


# Runtime
# 722 ms
# Beats
# 96.3%
# Memory
# 28.8 MB
# Beats
# 43.24%
# https://leetcode.com/problems/frog-jump-ii/solutions/2897985/java-o-n-explained/
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        result1 = max(stones[i] - stones[i-2] for i in range(2, n, 2)) if n > 2 else 0
        result2 = stones[1] - stones[0]
        result3 = max(stones[i] - stones[i-2] for i in range(3, n, 2)) if n > 3 else 0
        return max(result1, result2, result3)




tests = [
    [[0,3], 3],
    [[0,2,5,6,7], 5],
    [[0,3,9], 9],
]

run_functional_tests(Solution().maxJump, tests)
