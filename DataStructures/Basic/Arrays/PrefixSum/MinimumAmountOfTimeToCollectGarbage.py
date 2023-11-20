"""
https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/?envType=daily-question&envId=2023-11-20

You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.



Example 1:

Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
Output: 21
Explanation:
The paper garbage truck:
1. Travels from house 0 to house 1
2. Collects the paper garbage at house 1
3. Travels from house 1 to house 2
4. Collects the paper garbage at house 2
Altogether, it takes 8 minutes to pick up all the paper garbage.
The glass garbage truck:
1. Collects the glass garbage at house 0
2. Travels from house 0 to house 1
3. Travels from house 1 to house 2
4. Collects the glass garbage at house 2
5. Travels from house 2 to house 3
6. Collects the glass garbage at house 3
Altogether, it takes 13 minutes to pick up all the glass garbage.
Since there is no metal garbage, we do not need to consider the metal garbage truck.
Therefore, it takes a total of 8 + 13 = 21 minutes to collect all the garbage.
Example 2:

Input: garbage = ["MMM","PGM","GP"], travel = [3,10]
Output: 37
Explanation:
The metal garbage truck takes 7 minutes to pick up all the metal garbage.
The paper garbage truck takes 15 minutes to pick up all the paper garbage.
The glass garbage truck takes 15 minutes to pick up all the glass garbage.
It takes a total of 7 + 15 + 15 = 37 minutes to collect all the garbage.


Constraints:

2 <= garbage.length <= 105
garbage[i] consists of only the letters 'M', 'P', and 'G'.
1 <= garbage[i].length <= 10
travel.length == garbage.length - 1
1 <= travel[i] <= 100
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         n = len(garbage)
#         garbage_counts = [[0, 0 ,0] for _ in range(n)]
#         for i in range(n):
#             for c in garbage[i]:
#                 if c == 'P':
#                     garbage_counts[i][0] += 1
#                 elif c == 'M':
#                     garbage_counts[i][1] += 1
#                 elif c == 'G':
#                     garbage_counts[i][2] += 1
#         result = sum(garbage_counts[0])
#         deferred = [0, 0, 0]
#         for i in range(1, n):
#             for j in range(3):
#                 if garbage_counts[i][j] > 0:
#                     result += deferred[j] + travel[i-1]
#                     result += garbage_counts[i][j]
#                     deferred[j] = 0
#                 else:
#                     deferred[j] += garbage_counts[i][j]
#         return result

# Runtime
# 905
# ms
# Beats
# 59.34%
# of users with Python3
# Memory
# 39.27
# MB
# Beats
# 61.98%
# of users with Python3
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/editorial/?envType=daily-question&envId=2023-11-20
# class Solution:
#     def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
#         n = len(garbage)
#         prefix = [0] * (len(travel) + 1)
#         for i in range(len(travel)):
#             prefix[i+1] = prefix[i] + travel[i]
#         garbage_last_pos = {}
#         garbage_count = defaultdict(int)
#         for i in range(n):
#             for c in garbage[i]:
#                 garbage_last_pos[c] = i
#                 garbage_count[c] = garbage_count[c] + 1
#
#         result = 0
#         for c in "MPG":
#             if c in garbage_count:
#                 result += prefix[garbage_last_pos[c]] + garbage_count[c]
#         return result


# Runtime
# 869
# ms
# Beats
# 71.73%
# of users with Python3
# Memory
# 42.45
# MB
# Beats
# 6.94%
# of users with Python3
# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/editorial/?envType=daily-question&envId=2023-11-20
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]

        garbage_last_pos = defaultdict(int)
        result = 0

        for i in range(n):
            for c in garbage[i]:
                garbage_last_pos[c] = i
            result += len(garbage[i])

        for c in "MPG":
            if garbage_last_pos[c]:
                result += travel[garbage_last_pos[c]-1]
        return result


tests = [
    [["G","P","GP","GG"], [2,4,3], 21],
    [["MMM","PGM","GP"], [3,10], 37],
]

run_functional_tests(Solution().garbageCollection, tests)
