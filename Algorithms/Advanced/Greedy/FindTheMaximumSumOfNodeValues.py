"""
https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/?envType=daily-question&envId=2024-05-19

There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.



Example 1:


Input: nums = [1,2,1], k = 3, edges = [[0,1],[0,2]]
Output: 6
Explanation: Alice can achieve the maximum sum of 6 using a single operation:
- Choose the edge [0,2]. nums[0] and nums[2] become: 1 XOR 3 = 2, and the array nums becomes: [1,2,1] -> [2,2,2].
The total sum of values is 2 + 2 + 2 = 6.
It can be shown that 6 is the maximum achievable sum of values.
Example 2:


Input: nums = [2,3], k = 7, edges = [[0,1]]
Output: 9
Explanation: Alice can achieve the maximum sum of 9 using a single operation:
- Choose the edge [0,1]. nums[0] becomes: 2 XOR 7 = 5 and nums[1] become: 3 XOR 7 = 4, and the array nums becomes: [2,3] -> [5,4].
The total sum of values is 5 + 4 = 9.
It can be shown that 9 is the maximum achievable sum of values.
Example 3:


Input: nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
Output: 42
Explanation: The maximum achievable sum is 42 which can be achieved by Alice performing no operations.


Constraints:

2 <= n == nums.length <= 2 * 104
1 <= k <= 109
0 <= nums[i] <= 109
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
The input is generated such that edges represent a valid tree.
"""
import math
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1148
# ms
# Beats
# 13.64%
# of users with Python3
# Memory
# 46.10
# MB
# Beats
# 5.11%
# of users with Python3
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/editorial/?envType=daily-question&envId=2024-05-19
# class Solution:
#     def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
#
#         @cache
#         def impl(index, is_even):
#             if index == len(nums):
#                 return 0 if is_even else -math.inf
#
#             no_xor_done = nums[index] + impl(index+1, is_even)
#             xor_done = (nums[index] ^ k) + impl(index+1, 1 - is_even)
#             return max(xor_done, no_xor_done)
#
#         return impl(0, 1)


# Runtime
# 1056
# ms
# Beats
# 27.84%
# of users with Python3
# Memory
# 28.07
# MB
# Beats
# 67.05%
# of users with Python3
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/editorial/?envType=daily-question&envId=2024-05-19
# class Solution:
#     def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
#         n = len(nums)
#         dp = [[0] * 2 for _ in range(n+1)]
#         dp[n][1] = 0
#         dp[n][0] = -math.inf
#         for index in range(n-1, -1, -1):
#             for is_even in range(2):
#                 perform_operation = dp[index+1][1 - is_even] + (nums[index] ^ k)
#                 dont_perform = dp[index+1][is_even] + nums[index]
#                 dp[index][is_even] = max(perform_operation, dont_perform)
#         return dp[0][1]


# Runtime
# 950
# ms
# Beats
# 81.82%
# of users with Python3
# Memory
# 28.23
# MB
# Beats
# 38.07%
# of users with Python3
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/editorial/?envType=daily-question&envId=2024-05-19
# class Solution:
#     def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
#         n = len(nums)
#         net_change = [(nums[i] ^ k) - nums[i] for i in range(n)]
#         node_sum = sum(nums)
#
#         net_change.sort(reverse=True)
#
#         for i in range(0, n, 2):
#             if i+1 == n:
#                 break
#             pair_sum = net_change[i] + net_change[i+1]
#             if pair_sum > 0:
#                 node_sum += pair_sum
#         return node_sum


# Runtime
# 979
# ms
# Beats
# 40.34%
# of users with Python3
# Memory
# 28.00
# MB
# Beats
# 84.66%
# of users with Python3
# class Solution:
#     def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
#         n = len(nums)
#         net_change = [(nums[i] ^ k) - nums[i] for i in range(n)]
#         node_sum = sum(nums)
#
#         net_change.sort(reverse=True)
#
#         for i in range(0, n, 2):
#             if i+1 == n:
#                 break
#             pair_sum = net_change[i] + net_change[i+1]
#             node_sum += max(pair_sum, 0)
#         return node_sum


# Runtime
# 913
# ms
# Beats
# 100.00%
# of users with Python3
# Memory
# 28.14
# MB
# Beats
# 50.57%
# of users with Python3
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/editorial/?envType=daily-question&envId=2024-05-19
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sum_val, count = 0, 0
        pos_min = 1 << 30
        neg_max = -1 * (1 << 30)

        for node_value in nums:
            operated_node_val = node_value ^ k
            sum_val += node_value
            net_change = operated_node_val - node_value
            if net_change > 0:
                pos_min = min(pos_min, net_change)
                sum_val += net_change
                count += 1
            else:
                neg_max = max(neg_max, net_change)

        if count % 2 == 0:
            return sum_val

        return max(sum_val - pos_min, sum_val + neg_max)


tests = [
    [[1,2,1], 3, [[0,1],[0,2]], 6],
    [[2,3], 7, [[0,1]], 9],
    [[7,7,7,7,7,7], 3, [[0,1],[0,2],[0,3],[0,4],[0,5]], 42],
]

run_functional_tests(Solution().maximumValueSum, tests)
