"""
https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.



Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.


Constraints:

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106
"""
from typing import List

from numpy import cumsum

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def minCost(self, nums: List[int], cost: List[int]) -> int:
#         numAndCost = [(v, c) for v, c in zip(nums, cost)]
#         numAndCost.sort()
#         n = len(nums)
#         price1, price2 = [0] * n, [0] * n
#         # sums1, sums2 = [v for v in cumsum(v for v, c in numAndCost)], [v for v in reversed(cumsum(v for v, c in reversed(numAndCost)))]
#         sums1, sums2 = [0] * n, [0] * n
#         sums1[0], sums2[-1] = numAndCost[0][0], numAndCost[-1][0]
#         for i in range(1, n):
#             sums1[i] = sums1[i-1] + numAndCost[i][0]
#             i1 = n - 1 - i
#             sums2[i1] = sums2[i1 - 1] + numAndCost[i1][0]
#         for i in range(1, n):
#             price1[i] = price1[i-1] + (numAndCost[i][0] - numAndCost[i-1][0]) * sums1[i-1] * i
#             i1 = n-1-i
#             price2[i1] = price2[i1+1] + (numAndCost[i1+1][0] - numAndCost[i1][0]) * sums2[i1+1] * i
#         return 0


# Runtime
# 476 ms
# Beats
# 67.65%
# Memory
# 39.3 MB
# Beats
# 33.82%
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/editorial/
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        numAndCost = [(v, c) for v, c in zip(nums, cost)]
        numAndCost.sort()
        n = len(nums)
        prefix_cost = [0] * n
        prefix_cost[0] = numAndCost[0][1]
        for i in range(1, n):
            prefix_cost[i] = prefix_cost[i-1] + numAndCost[i][1]

        total_cost = 0
        for i in range(1, n):
            total_cost += numAndCost[i][1] * (numAndCost[i][0] - numAndCost[0][0])

        result = total_cost
        for i in range(1, n):
            gap = numAndCost[i][0] - numAndCost[i-1][0]
            total_cost += prefix_cost[i-1] * gap
            total_cost -= gap * (prefix_cost[n-1] - prefix_cost[i-1])
            result = min(result, total_cost)

        return result



"""
1 3 5 2
2 4 1 14

1(2) 2(14) 3(4) 5(1)
0      2   14+4 4*2+14*3+2*4    
"""


tests = [
    [[1,3,5,2], [2,3,1,14], 8],
    [[2,2,2,2,2], [4,2,8,1,3], 0],
]

run_functional_tests(Solution().minCost, tests)
