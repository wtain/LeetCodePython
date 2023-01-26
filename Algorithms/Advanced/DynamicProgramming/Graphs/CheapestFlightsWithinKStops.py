"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.



Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 442 ms
# Beats
# 14.64%
# Memory
# 15.2 MB
# Beats
# 73.37%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        big_value = float('Inf')
        dp = [[big_value for __ in range(n)] for _ in range(2)]
        T = 0
        dp[T][src] = 0

        for i in range(k+1):
            dp[1-T] = dp[T].copy()
            for u, v, w in flights:
                dp[1-T][v] = min(dp[1-T][v], dp[T][u] + w)
            T = 1 - T
        return dp[T][dst] if dp[T][dst] != big_value else -1


tests = [
    [4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1, 700],
    [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1, 200],
    [3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0, 500],
]

run_functional_tests(Solution().findCheapestPrice, tests)
