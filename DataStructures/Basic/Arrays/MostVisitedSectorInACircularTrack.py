"""
https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).



Example 1:


Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.
Example 2:

Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
Output: [2]
Example 3:

Input: n = 7, rounds = [1,3,5,7]
Output: [1,2,3,4,5,6,7]


Constraints:

2 <= n <= 100
1 <= m <= 100
rounds.length == m + 1
1 <= rounds[i] <= n
rounds[i] != rounds[i + 1] for 0 <= i < m
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 68 ms, faster than 39.93% of Python3 online submissions for Most Visited Sector in a Circular Track.
# Memory Usage: 14.4 MB, less than 30.20% of Python3 online submissions for Most Visited Sector in a Circular Track.
# class Solution:
#     def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
#         sectors = [0] * n
#         for i, j in zip(rounds, rounds[1:]):
#             if j < i:
#                 j += n
#             for k in range(i, j):
#                 sectors[(k-1) % n] += 1
#         sectors[rounds[-1] - 1] += 1
#         mx = max(sectors)
#         return [i+1 for i,v in enumerate(sectors) if v == mx]


# Runtime: 40 ms, faster than 87.92% of Python3 online submissions for Most Visited Sector in a Circular Track.
# Memory Usage: 14 MB, less than 92.62% of Python3 online submissions for Most Visited Sector in a Circular Track.
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        if s == e:
            return [s]
        elif s < e:
            return list(range(s, e+1))
        else:
            return list(range(1, e+1)) + list(range(s, n+1))


tests = [
    [4, [1,3,1,2], [1,2]],
    [2, [2,1,2,1,2,1,2,1,2], [2]],
    [7, [1,3,5,7], [1,2,3,4,5,6,7]]
]

run_functional_tests(Solution().mostVisited, tests)