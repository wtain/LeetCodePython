"""
https://leetcode.com/problems/closest-dessert-cost/

You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:

There must be exactly one ice cream base.
You can add one or more types of topping or have no toppings at all.
There are at most two of each type of topping.
You are given three inputs:

baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
target, an integer representing your target price for dessert.
You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.



Example 1:

Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.
Example 2:

Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
Output: 17
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.
Example 3:

Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
Output: 8
Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.


Constraints:

n == baseCosts.length
m == toppingCosts.length
1 <= n, m <= 10
1 <= baseCosts[i], toppingCosts[i] <= 104
1 <= target <= 104
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#         closest_cost = 0
#
#         def check_cost(cost: int, target: int):
#             nonlocal closest_cost
#             if abs(cost-target) < abs(closest_cost-target) or \
#                abs(cost - target) == abs(closest_cost - target) and cost < closest_cost:
#                 closest_cost = cost
#
#         def try_toppings(toppings_target: int):
#
#
#         for base_cost in baseCosts:
#             try_toppings(target-base_cost)
#
#         return closest_cost

# TLE
# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#         used_toppings = [0] * len(toppingCosts)
#         closest_cost = float('Inf')
#
#         def check_toppings(base: int):
#             nonlocal used_toppings, closest_cost
#             if abs(base-target) < abs(closest_cost-target) or \
#                abs(base - target) == abs(closest_cost - target) and base < closest_cost:
#                 closest_cost = base
#             if base > target and abs(base-target) >= abs(closest_cost-target):
#                 return
#             for i, t in enumerate(toppingCosts):
#                 if used_toppings[i] < 2:
#                     used_toppings[i] += 1
#                     check_toppings(base + toppingCosts[i])
#                     used_toppings[i] -= 1
#
#         for base in baseCosts:
#             check_toppings(base)
#
#         return closest_cost


# TLE
# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#         used_toppings = [0] * len(toppingCosts)
#
#         def check_toppings(toppings_target: int) -> int:
#             nonlocal used_toppings
#             if toppings_target <= 0:
#                 return 0
#             best_topings_cost = 0
#             for i, t in enumerate(toppingCosts):
#                 if used_toppings[i] < 2:
#                     used_toppings[i] += 1
#                     topings_cost = check_toppings(toppings_target - toppingCosts[i]) + toppingCosts[i]
#                     used_toppings[i] -= 1
#                     if abs(topings_cost-toppings_target) < abs(best_topings_cost-toppings_target) or \
#                        abs(topings_cost-toppings_target) == abs(best_topings_cost-toppings_target) and \
#                             topings_cost < best_topings_cost:
#                         best_topings_cost = topings_cost
#             return best_topings_cost
#
#         best_price = float('Inf')
#
#         for base in baseCosts:
#             cost = base + check_toppings(target - base)
#             if abs(cost-target) < abs(best_price-target):
#                 best_price = cost
#
#         return best_price

# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#         used_toppings = [0] * len(toppingCosts)
#
#         def check_toppings(toppings_target: int) -> int:
#             nonlocal used_toppings
#             # Knapsack or something similar??
#             if toppings_target <= 0:
#                 return 0
#             best_topings_cost = 0
#             for i, t in enumerate(toppingCosts):
#                 if used_toppings[i] < 2:
#                     used_toppings[i] += 1
#                     topings_cost = check_toppings(toppings_target - toppingCosts[i]) + toppingCosts[i]
#                     used_toppings[i] -= 1
#                     if abs(topings_cost-toppings_target) < abs(best_topings_cost-toppings_target) or \
#                        abs(topings_cost-toppings_target) == abs(best_topings_cost-toppings_target) and \
#                             topings_cost < best_topings_cost:
#                         best_topings_cost = topings_cost
#             return best_topings_cost
#
#         best_price = float('Inf')
#
#         for base in baseCosts:
#             cost = base + check_toppings(target - base)
#             if abs(cost-target) < abs(best_price-target):
#                 best_price = cost
#
#         return best_price


# Runtime
# 69 ms
# Beats
# 86.45%
# Memory
# 22.7 MB
# Beats
# 19.41%
# https://leetcode.com/problems/closest-dessert-cost/solutions/3131919/you-can-make-it-using-dp-cpp/
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        def impl(i: int, s: int):
            nonlocal dp, maxi, toppingCosts, target, diff1

            if abs(target-s) < diff1:
                maxi = s
                diff1 = abs(target-s)
            elif abs(target - s) == diff1:
                maxi = min(maxi, s)

            if s > target:
                return

            if i >= len(toppingCosts):
                return

            if dp[i][s] != -1:
                return

            impl(i+1, s)
            impl(i+1, s+toppingCosts[i])
            impl(i+1, s+2*toppingCosts[i])

            dp[i][s] = 1

        result, diff = 0, float('Inf')
        for cost in baseCosts:
            dp = [[-1] * (target+1) for _ in range(len(toppingCosts))]
            maxi = 0
            diff1 = float('Inf')
            impl(0, cost)

            if abs(target-maxi) < diff:
                result = maxi
                diff = abs(target-maxi)
            elif abs(target - maxi) == diff:
                result = min(result, maxi)

        return result


# class Solution:
#     def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#
#         @cache
#         def impl(i: int, s: int) -> (int, int):
#             nonlocal toppingCosts, target
#
#             maxi, diff1 = 0, float('Inf')
#
#             def update_best(s: int):
#                 nonlocal maxi, diff1
#                 if abs(target-s) < diff1:
#                     maxi = s
#                     diff1 = abs(target-s)
#                 elif abs(target - s) == diff1:
#                     maxi = min(maxi, s)
#
#             update_best(s)
#
#             if s > target:
#                 return float('Inf'), float('Inf')
#
#             if i >= len(toppingCosts):
#                 return float('Inf'), float('Inf')
#
#             maxi2, diff2 = impl(i+1, s)
#             maxi3, diff3 = impl(i+1, s+toppingCosts[i])
#             maxi4, diff4 = impl(i+1, s+2*toppingCosts[i])
#             update_best(maxi2)
#             update_best(maxi3)
#             update_best(maxi4)
#
#             return maxi, diff1
#
#         result, diff = 0, float('Inf')
#         for cost in baseCosts:
#             maxi, diff1 = impl(0, cost)
#
#             if abs(target-maxi) < diff:
#                 result = maxi
#                 diff = abs(target-maxi)
#             elif abs(target - maxi) == diff:
#                 result = min(result, maxi)
#
#         return result


tests = [
    [[52,48,17,44,33,17,58,52], [74,28,20,98,46,9,1,1,22,2], 93, 93],
    [[10], [1], 1, 10],
    [[1,7], [3,4], 10, 10],
    [[2,3], [4,5,100], 18, 17],
    [[3,10], [2,5], 9, 8],
]

run_functional_tests(Solution().closestCost, tests)
# run_functional_tests(Solution().closestCost, tests, run_tests=4)
# run_functional_tests(Solution().closestCost, tests, run_tests=5)
