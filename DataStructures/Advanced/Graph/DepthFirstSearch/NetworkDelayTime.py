"""
https://leetcode.com/problems/network-delay-time/


You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
import heapq
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 491 ms, faster than 82.46% of Python3 online submissions for Network Delay Time.
# Memory Usage: 16.1 MB, less than 76.55% of Python3 online submissions for Network Delay Time.
# https://leetcode.com/submissions/detail/185930157/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        transitions = defaultdict(set)
        for u, v, w in times:
            transitions[u].add((v, w))

        dist = {}
        to_visit = []
        heapq.heappush(to_visit, (0, k))
        while to_visit:
            current_time, current_id = heapq.heappop(to_visit)
            if current_id in dist:
                continue
            dist[current_id] = current_time
            for node, t in transitions[current_id]:
                if node in dist:
                    continue
                heapq.heappush(to_visit, (t+current_time, node))
        if len(dist) != n:
            return -1
        mx = -1
        for dk in dist:
            mx = max(dist[dk], mx)
        return mx


tests = [
    [[[1,2,1],[2,3,2],[1,3,2]], 3, 1, 2],
    [[[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2],
    [[[1,2,1]], 2, 1, 1],
    [[[1,2,1]], 2, 2, -1]
]

run_functional_tests(Solution().networkDelayTime, tests)
