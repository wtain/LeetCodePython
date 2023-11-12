"""
https://leetcode.com/problems/bus-routes/description/?envType=daily-question&envId=2023-11-12

repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.



Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""
import math
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 7912ms
# Beats 5.04%of users with Python3
# Memory
# Details
# 48.15MB
# Beats 52.10%of users with Python3
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stops = defaultdict(set)
        initial = []
        finish = set()
        for i, route in enumerate(routes):
            for stop in route:
                if stop == source:
                    initial.append(i)
                if stop == target:
                    finish.add(i)
                stops[stop].add(i)
        transitions = defaultdict(set)
        for stop in stops:
            adj = stops[stop]
            for r1 in adj:
                for r2 in adj:
                    if r1 == r2:
                        continue
                    transitions[r1].add(r2)
                    transitions[r2].add(r1)

        def dfs(i):
            visited = set()
            current = [(i, 1)]
            while current:
                next_level = []
                for state in current:
                    route, hops = state
                    if route in finish:
                        return hops
                    for next_route in transitions[route]:
                        if next_route in visited:
                            continue
                        visited.add(next_route)
                        next_level.append((next_route, hops+1))
                current = next_level
            return math.inf

        shortest = min(dfs(r) for r in initial)
        return shortest if shortest != math.inf else -1


# https://leetcode.com/problems/bus-routes/editorial/?envType=daily-question&envId=2023-11-12
# class Solution:
#     def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
#         if source == target:
#             return 0
#         stops = defaultdict(set)
#         initial = []
#         finish = set()
#         for i, route in enumerate(routes):
#             route.sort()
#             for stop in route:
#                 if stop == source:
#                     initial.append(i)
#                 if stop == target:
#                     finish.add(i)
#                 stops[stop].add(i)
#         transitions = defaultdict(set)
#         for stop in stops:
#             adj = stops[stop]
#             for r1 in adj:
#                 for r2 in adj:
#                     if r1 == r2:
#                         continue
#                     transitions[r1].add(r2)
#                     transitions[r2].add(r1)
#
#         def dfs(i):
#             visited = set()
#             current = [(i, 1)]
#             while current:
#                 next_level = []
#                 for state in current:
#                     route, hops = state
#                     if route in finish:
#                         return hops
#                     for next_route in transitions[route]:
#                         if next_route in visited:
#                             continue
#                         visited.add(next_route)
#                         next_level.append((next_route, hops+1))
#                 current = next_level
#             return math.inf
#
#         shortest = min(dfs(r) for r in initial)
#         return shortest if shortest != math.inf else -1


tests = [
    [[[1,2,7],[3,6,7]], 1, 6, 2],
    [[[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12, -1],
    [[[1,7],[3,5]], 5, 5, 0],
    [[[2],[2,8]], 8, 2, 1],
]

run_functional_tests(Solution().numBusesToDestination, tests)
