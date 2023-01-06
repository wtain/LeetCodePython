"""
https://leetcode.com/problems/maximum-ice-cream-bars/description/

It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.



Example 1:

Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.
Example 3:

Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.


Constraints:

costs.length == n
1 <= n <= 105
1 <= costs[i] <= 105
1 <= coins <= 108
"""
import bisect
from collections import Counter
from itertools import accumulate
from typing import List

from numpy import cumsum

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 925 ms
# Beats
# 57.7%
# Memory
# 28.1 MB
# Beats
# 17.54%
# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         costs.sort()
#         totals = list(accumulate(costs))
#         return bisect.bisect_right(totals, coins)


# Runtime
# 868 ms
# Beats
# 79.32%
# Memory
# 29.7 MB
# Beats
# 17.54%
# https://leetcode.com/problems/maximum-ice-cream-bars/solutions/2885725/maximum-ice-cream-bars/c
# class Solution:
#     def maxIceCream(self, costs: List[int], coins: int) -> int:
#         icecreams = 0
#         frequencies = Counter(costs)
#         for cost in sorted(frequencies.keys()):
#             if cost > coins:
#                 break
#             count = min(frequencies[cost], coins // cost)
#             coins -= cost * count
#             icecreams += count
#         return icecreams


# Runtime
# 880 ms
# Beats
# 72.51%
# Memory
# 28 MB
# Beats
# 61.26%
# https://leetcode.com/problems/maximum-ice-cream-bars/solutions/2885725/maximum-ice-cream-bars/c
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        icecreams = 0
        m = max(costs)
        frequencies = [0] * (m+1)
        for cost in costs:
            frequencies[cost] += 1
        for cost in range(1, m+1):
            if cost > coins:
                break
            count = min(frequencies[cost], coins // cost)
            coins -= cost * count
            icecreams += count
        return icecreams


tests = [
    [[1,3,2,4,1], 7, 4],
    [[10,6,8,7,7,8], 5, 0],
    [[1,6,3,1,2,5], 20, 6],
    [[8,2,10,2,5,4,2,6,3,8], 46, 9],
]

run_functional_tests(Solution().maxIceCream, tests)
