"""
https://leetcode.com/problems/last-stone-weight-ii/

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
Example 2:

Input: stones = [31,26,33,21,40]
Output: 5


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 100
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 38 ms
# Beats
# 97.62%
# Memory
# 14.3 MB
# Beats
# 40.65%
# # https://leetcode.com/problems/last-stone-weight-ii/solutions/294888/java-c-python-easy-knapsacks-dp/
# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         dp = {0}
#         sumA = sum(stones)
#         for stone in stones:
#             dp |= {stone + i for i in dp}
#         return min(abs(sumA - i - i) for i in dp)


# Runtime
# 50 ms
# Beats
# 88.61%
# Memory
# 14.1 MB
# Beats
# 56.80%
# https://leetcode.com/problems/last-stone-weight-ii/solutions/294888/java-c-python-easy-knapsacks-dp/
# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         dp = {0}
#         for stone in stones:
#             dp = {stone + x for x in dp} | {abs(stone - x) for x in dp}
#         return min(dp)


# Runtime
# 37 ms
# Beats
# 98.30%
# Memory
# 14.1 MB
# Beats
# 50%
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        return min(reduce(lambda dp, stone: {stone + x for x in dp} | {abs(stone - x) for x in dp}, stones, {0}))


tests = [
    [[2,7,4,1,8,1], 1],
    [[31,26,33,21,40], 5],
]

run_functional_tests(Solution().lastStoneWeightII, tests)
