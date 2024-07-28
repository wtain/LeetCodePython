"""
https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/?envType=daily-question&envId=2024-07-28

A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.


Example 1:

       
Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.
Example 2:


Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.


Constraints:

2 <= n <= 104
n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
There are no duplicate edges.
Each vertex can be reached directly or indirectly from every other vertex.
1 <= time, change <= 103
"""
import heapq
import math
from collections import defaultdict, deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2030
# ms
# Beats
# 30.46%
# Analyze Complexity
# Memory
# 26.63
# MB
# Beats
# 29.80%
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/editorial/?envType=daily-question&envId=2024-07-28
# class Solution:
#     def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
#         adj = defaultdict(list)
#         for a, b in edges:
#             adj[a].append(b)
#             adj[b].append(a)
#         dist1 = [math.inf] * (n+1)
#         dist2 = [math.inf] * (n+1)
#         freq = [0] * (n+1)
#
#         pq = []
#         heapq.heappush(pq, [0, 1])
#         dist1[1] = 0
#
#         while pq:
#             time_taken, node = heapq.heappop(pq)
#             freq[node] += 1
#             if freq[node] == 2 and node == n:
#                 return time_taken
#             if (time_taken // change) % 2 == 1:
#                 time_taken = change * (time_taken // change+1) + time
#             else:
#                 time_taken = time_taken + time
#
#             for neighbor in adj[node]:
#                 if freq[neighbor] == 2:
#                     continue
#                 if dist1[neighbor] > time_taken:
#                     dist2[neighbor] = dist1[neighbor]
#                     dist1[neighbor] = time_taken
#                     heapq.heappush(pq, [time_taken, neighbor])
#                 elif dist2[neighbor] > time_taken and dist1[neighbor] != time_taken:
#                     dist2[neighbor] = time_taken
#                     heapq.heappush(pq, [time_taken, neighbor])
#
#         return 0

# Runtime
# 3006
# ms
# Beats
# 8.60%
# Analyze Complexity
# Memory
# 26.18
# MB
# Beats
# 93.38%
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/solutions/5546196/detailed-easy-java-python3-c-solution-218-ms/?envType=daily-question&envId=2024-07-28
# class Solution:
#     def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
#         adj = defaultdict(list)
#         for a, b in edges:
#             adj[a].append(b)
#             adj[b].append(a)
#         dist = [-1] * (n+1)
#         freq = [0] * (n+1)
#
#         pq = []
#         heapq.heappush(pq, [0, 1])
#
#         while pq:
#             time_taken, node = heapq.heappop(pq)
#
#             if dist[node] == time_taken or freq[node] >= 2:
#                 continue
#             freq[node] += 1
#             dist[node] = time_taken
#
#             if freq[node] == 2 and node == n:
#                 return dist[node]
#
#             if (time_taken // change) % 2 != 0:
#                 time_taken = change * (time_taken // change+1)
#
#             for neighbor in adj[node]:
#                 heapq.heappush(pq, [time_taken + time, neighbor])
#
#         return -1


# Runtime
# 1664
# ms
# Beats
# 96.69%
# Analyze Complexity
# Memory
# 26.10
# MB
# Beats
# 93.38%
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/editorial/?envType=daily-question&envId=2024-07-28
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        dist1 = [-1] * (n+1)
        dist2 = [-1] * (n+1)
        q = deque()
        q.append([1, 1])
        dist1[1] = 0

        while q:
            node, freq = q.popleft()

            time_taken = dist1[node] if freq == 1 else dist2[node]
            if (time_taken // change) % 2 == 1:
                time_taken = change * (time_taken // change + 1) + time
            else:
                time_taken = time_taken + time

            for neighbor in adj[node]:
                if dist1[neighbor] == -1:
                    dist1[neighbor] = time_taken
                    q.append([neighbor, 1])
                elif dist2[neighbor] == -1 and dist1[neighbor] != time_taken:
                    if neighbor == n:
                        return time_taken
                    dist2[neighbor] = time_taken
                    q.append([neighbor, 2])
        return 0


tests = [
    [5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5, 13],
    [2, [[1,2]], 3, 2, 11],
]

run_functional_tests(Solution().secondMinimum, tests)
