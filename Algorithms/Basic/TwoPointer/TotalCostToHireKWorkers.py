"""
https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
A worker can only be chosen once.
Return the total cost to hire exactly k workers.



Example 1:

Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
- In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
- In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
The total hiring cost is 11.
Example 2:

Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4
Explanation: We hire 3 workers in total. The total cost is initially 0.
- In the first hiring round we choose the worker from [1,2,4,1]. The lowest cost is 1, and we break the tie by the smallest index, which is 0. The total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common in the first and last 3 workers.
- In the second hiring round we choose the worker from [2,4,1]. The lowest cost is 1 (index 2). The total cost = 1 + 1 = 2.
- In the third hiring round there are less than three candidates. We choose the worker from the remaining workers [2,4]. The lowest cost is 2 (index 0). The total cost = 2 + 2 = 4.
The total hiring cost is 4.


Constraints:

1 <= costs.length <= 105
1 <= costs[i] <= 105
1 <= k, candidates <= costs.length
"""
import heapq
from heapq import heapify, heappop, heappush
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 804 ms
# Beats
# 72.89%
# Memory
# 27 MB
# Beats
# 62.15%
# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         n = len(costs)
#         leftHeap, rightHeap = costs[:candidates], costs[max(candidates, n - candidates):]
#         heapify(leftHeap)
#         heapify(rightHeap)
#
#         result = 0
#         l, r = candidates, n - candidates - 1
#         for i in range(k):
#             if not rightHeap or leftHeap and leftHeap[0] <= rightHeap[0]:
#                 result += heapq.heappop(leftHeap)
#                 if l <= r:
#                     heapq.heappush(leftHeap, costs[l])
#                     l += 1
#             else:
#                 result += heapq.heappop(rightHeap)
#                 if l <= r:
#                     heapq.heappush(rightHeap, costs[r])
#                     r -= 1
#         return result


# Runtime
# 789 ms
# Beats
# 80.54%
# Memory
# 27 MB
# Beats
# 62.15%
# https://leetcode.com/problems/total-cost-to-hire-k-workers/editorial/
# class Solution:
#     def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#         n = len(costs)
#         head_workers = costs[:candidates]
#         tail_workers = costs[max(candidates, n - candidates):]
#         heapify(head_workers)
#         heapify(tail_workers)
#
#         result = 0
#         l, r = candidates, n - 1 - candidates
#         for i in range(k):
#             if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
#                 result += heappop(head_workers)
#                 if l <= r:
#                     heappush(head_workers, costs[l])
#                     l += 1
#             else:
#                 result += heappop(tail_workers)
#                 if l <= r:
#                     heappush(tail_workers, costs[r])
#                     r -= 1
#         return result

# Runtime
# 905 ms
# Beats
# 45.77%
# Memory
# 28.5 MB
# Beats
# 36.24%
# https://leetcode.com/problems/total-cost-to-hire-k-workers/editorial/
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, n - candidates), n):
            pq.append((costs[i], 1))

        heapify(pq)
        result = 0
        l, r = candidates, n - candidates - 1
        for i in range(k):
            cost, section = heappop(pq)
            result += cost
            if l <= r:
                if section == 0:
                    heappush(pq, (costs[l], 0))
                    l += 1
                else:
                    heappush(pq, (costs[r], 1))
                    r -= 1
        return result


tests = [
    [[18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75],
        13,
        23, 223],
    [[17,12,10,2,7,2,11,20,8], 3, 4, 11],
    [[1,2,4,1], 3, 3, 4],
]

run_functional_tests(Solution().totalCost, tests)
