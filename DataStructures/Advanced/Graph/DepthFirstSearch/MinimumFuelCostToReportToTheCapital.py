"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.



Example 1:


Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation:
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum.
It can be proven that 3 is the minimum number of liters of fuel needed.
Example 2:


Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation:
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum.
It can be proven that 7 is the minimum number of liters of fuel needed.
Example 3:


Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.


Constraints:

1 <= n <= 105
roads.length == n - 1
roads[i].length == 2
0 <= ai, bi < n
ai != bi
roads represents a valid tree.
1 <= seats <= 105
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
#         neighbors = defaultdict(list)
#         for a, b in roads:
#             neighbors[a].append(b)
#             neighbors[b].append(a)
#
#         leaves = []
#         level = [0]
#         visited = set()
#         depth, max_depth = 0, 0
#         while level:
#             next_level = []
#             for node in level:
#                 visited.add(node)
#                 if len(neighbors[node]) == 1 and neighbors[node][0] in visited:
#                     leaves.append((node, depth))
#                     max_depth = max(max_depth, depth)
#                 else:
#                     for child in neighbors[node]:
#                         if child in visited:
#                             continue
#                         next_level.append(child)
#             depth += 1
#             level = next_level
#
#         fuel_required = 0
#         cars = {city: 1 for city, depth in leaves if depth == max_depth}  # In each leave city we have a car with one (1) person
#         visited = set()
#         while cars:
#             next_cars = defaultdict(int)
#             for city in cars:
#                 fuel_required += (cars[city] - 1) // seats + 1
#                 visited.add(city)
#                 for neigbor in neighbors[city]:
#                     if neigbor in visited:
#                         continue
#                     if neigbor == 0:
#                         continue
#                     next_cars[neigbor] += cars[city]
#             for neigbor in next_cars:
#                 next_cars[neigbor] += 1
#             print([str(k) + ": " + str(next_cars[k]) for k in next_cars])
#             cars = next_cars
#         return fuel_required


# Runtime
# 1989 ms
# Beats
# 86.97%
# Memory
# 162.3 MB
# Beats
# 62.32%
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        neighbors = defaultdict(list)
        for a, b in roads:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city: int, parent: int) -> (int, int):
            nonlocal neighbors, seats
            fuel_required = 0
            people_total = 1
            for child in neighbors[city]:
                if child == parent:
                    continue
                fuel, people = dfs(child, city)
                fuel_required += fuel + (people - 1) // seats + 1
                people_total += people
            return fuel_required, people_total

        fuel_required = dfs(0, -1)[0]
        return fuel_required


tests = [
    [[[1,0],[1,2],[3,2],[4,1],[0,5],[6,5],[5,7]], 7, 7],
    [[[1,0],[0,2],[3,1],[1,4],[5,0]], 1, 7],
    [[[0,1],[0,2],[0,3]], 5, 3],
    [[[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2, 7],
    [[], 1, 0],
]

run_functional_tests(Solution().minimumFuelCost, tests)
