"""
https://leetcode.com/problems/paint-house-iii/

There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.



Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.


Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 104



Define dp[i][j][k] as the minimum cost where we have k neighborhoods in the first i houses and the i-th house is painted with the color j.
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 3478 ms, faster than 22.48% of Python3 online submissions for Paint House III.
# Memory Usage: 39.3 MB, less than 33.33% of Python3 online submissions for Paint House III.
# https://leetcode.com/problems/paint-house-iii/solution/
# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         MAX_COST = 1000001
#         dp = [[[-2] * 21 for _ in range(100)] for _ in range(100)]
#
#         def impl(houses: List[int], cost: List[List[int]], targetCount: int, currIndex: int, neighborhoodCount: int, previousHouseColor: int) -> int:
#             if currIndex == len(houses):
#                 return 0 if neighborhoodCount == targetCount else MAX_COST
#
#             if neighborhoodCount > targetCount:
#                 return MAX_COST
#
#             if dp[currIndex][neighborhoodCount][previousHouseColor] != -2:
#                 return dp[currIndex][neighborhoodCount][previousHouseColor]
#
#             minCost = MAX_COST
#             if houses[currIndex] != 0:
#                 increment = 1 if houses[currIndex] != previousHouseColor else 0
#                 newNeighborhoodCount = neighborhoodCount + increment
#                 minCost = impl(houses, cost, targetCount, currIndex + 1, newNeighborhoodCount, houses[currIndex])
#             else:
#                 totalColors = len(cost[0])
#
#                 for color in range(1, totalColors+1):
#                     increment = 1 if color != previousHouseColor else 0
#                     newNeighborhoodCount = neighborhoodCount + increment
#                     currCost = cost[currIndex][color-1] + impl(houses, cost, targetCount, currIndex+1, newNeighborhoodCount, color)
#                     minCost = min(minCost, currCost)
#
#             dp[currIndex][neighborhoodCount][previousHouseColor] = minCost
#             return minCost
#
#         result = impl(houses, cost, target, 0, 0, 0)
#
#         return -1 if result == MAX_COST else result


# Runtime: 2419 ms, faster than 43.93% of Python3 online submissions for Paint House III.
# Memory Usage: 44.7 MB, less than 24.29% of Python3 online submissions for Paint House III.
# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         MAX_COST = 1000001
#
#         @lru_cache(None)
#         def impl(currIndex: int, neighborhoodCount: int, previousHouseColor: int) -> int:
#             if currIndex == len(houses):
#                 return 0 if neighborhoodCount == target else MAX_COST
#
#             if neighborhoodCount > target:
#                 return MAX_COST
#
#             minCost = MAX_COST
#             if houses[currIndex] != 0:
#                 increment = 1 if houses[currIndex] != previousHouseColor else 0
#                 newNeighborhoodCount = neighborhoodCount + increment
#                 minCost = impl(currIndex + 1, newNeighborhoodCount, houses[currIndex])
#             else:
#                 totalColors = len(cost[0])
#
#                 for color in range(1, totalColors+1):
#                     increment = 1 if color != previousHouseColor else 0
#                     newNeighborhoodCount = neighborhoodCount + increment
#                     currCost = cost[currIndex][color-1] + impl(currIndex+1, newNeighborhoodCount, color)
#                     minCost = min(minCost, currCost)
#
#             return minCost
#
#         result = impl(0, 0, 0)
#
#         return -1 if result == MAX_COST else result


# Runtime: 3536 ms, faster than 21.96% of Python3 online submissions for Paint House III.
# Memory Usage: 19.6 MB, less than 77.26% of Python3 online submissions for Paint House III.
# https://leetcode.com/problems/paint-house-iii/solution/
# class Solution:
#     def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
#         MAX_COST = 1000001
#         dp = [[[MAX_COST] * n for _ in range(target+1)] for _ in range(m)]
#
#         for color in range(1, n+1):
#             if houses[0] == color:
#                 dp[0][1][color-1] = 0
#             elif houses[0] == 0:
#                 dp[0][1][color-1] = cost[0][color-1]
#
#         for house in range(1, m):
#             for neighborhoods in range(1, min(target, house+1)+1):
#                 for color in range(1, n+1):
#                     if houses[house] != 0 and color != houses[house]:
#                         continue
#                     currCost = MAX_COST
#                     for prevColor in range(1, n+1):
#                         if prevColor != color:
#                             currCost = min(currCost, dp[house-1][neighborhoods-1][prevColor-1])
#                         else:
#                             currCost = min(currCost, dp[house - 1][neighborhoods][prevColor - 1])
#
#                     costToPaint = 0 if houses[house] != 0 else cost[house][color-1]
#                     dp[house][neighborhoods][color-1] = currCost + costToPaint
#
#         minCost = MAX_COST
#         for color in range(1, n+1):
#             minCost = min(minCost, dp[m-1][target][color-1])
#
#         return -1 if minCost == MAX_COST else minCost


# Runtime: 2639 ms, faster than 37.47% of Python3 online submissions for Paint House III.
# Memory Usage: 14.2 MB, less than 97.42% of Python3 online submissions for Paint House III.
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        MAX_COST = 1000001
        dp = [[MAX_COST] * n for _ in range(target+1)]

        for color in range(1, n+1):
            if houses[0] == color:
                dp[1][color-1] = 0
            elif houses[0] == 0:
                dp[1][color-1] = cost[0][color-1]

        for house in range(1, m):
            memo = [[MAX_COST] * n for _ in range(target+1)]

            for neighborhoods in range(1, min(target, house+1)+1):
                for color in range(1, n+1):
                    if houses[house] != 0 and color != houses[house]:
                        continue
                    currCost = MAX_COST
                    for prevColor in range(1, n+1):
                        if prevColor != color:
                            currCost = min(currCost, dp[neighborhoods-1][prevColor-1])
                        else:
                            currCost = min(currCost, dp[neighborhoods][prevColor - 1])

                    costToPaint = 0 if houses[house] != 0 else cost[house][color-1]
                    memo[neighborhoods][color-1] = currCost + costToPaint
            dp = memo

        minCost = MAX_COST
        for color in range(1, n+1):
            minCost = min(minCost, dp[target][color-1])

        return -1 if minCost == MAX_COST else minCost


tests = [
    [[0,0,0,0,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3, 9],
    [[0,2,1,2,0], [[1,10],[10,1],[10,1],[1,10],[5,1]], 5, 2, 3, 11],
    [[3,1,2,3], [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 4, 3, 3, -1]
]

run_functional_tests(Solution().minCost, tests)
