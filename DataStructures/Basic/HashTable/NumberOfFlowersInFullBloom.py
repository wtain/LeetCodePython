"""
https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=daily-question&envId=2023-10-11

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.



Example 1:


Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:


Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.


Constraints:

1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= people.length <= 5 * 104
1 <= people[i] <= 109
"""
import heapq
from bisect import bisect_right
from typing import List

from sortedcontainers import SortedDict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 900ms
# Beats 73.03%of users with Python3
# Memory
# Details
# 44.78MB
# Beats 41.82%of users with Python3
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/editorial/?envType=daily-question&envId=2023-10-11
# class Solution:
#     def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
#         flowers.sort()
#         sorted_people = sorted(people)
#         dic = {}
#         heap = []
#         i = 0
#         for person in sorted_people:
#             while i < len(flowers) and flowers[i][0] <= person:
#                 heapq.heappush(heap, flowers[i][1])
#                 i += 1
#             while heap and heap[0] < person:
#                 heapq.heappop(heap)
#             dic[person] = len(heap)
#         return [dic[x] for x in people]


# Runtime
# Details
# 1058ms
# Beats 30.00%of users with Python3
# Memory
# Details
# 45.15MB
# Beats 22.73%of users with Python3
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/editorial/?envType=daily-question&envId=2023-10-11
# class Solution:
#     def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
#         difference = SortedDict({0: 0})
#         for start, end in flowers:
#             difference[start] = difference.get(start, 0) + 1
#             difference[end+1] = difference.get(end+1, 0) - 1
#         positions = []
#         prefix = []
#         curr = 0
#         for key, val in difference.items():
#             positions.append(key)
#             curr += val
#             prefix.append(curr)
#         result = []
#         for person in people:
#             i = bisect_right(positions, person) - 1
#             result.append(prefix[i])
#         return result


# Runtime
# Details
# 903ms
# Beats 71.52%of users with Python3
# Memory
# Details
# 45.10MB
# Beats 22.73%of users with Python3
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/editorial/?envType=daily-question&envId=2023-10-11
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []
        for start, end in flowers:
            starts.append(start)
            ends.append(end+1)
        starts.sort()
        ends.sort()
        result = []
        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            result.append(i-j)
        return result


tests = [
    [[[1,6],[3,7],[9,12],[4,13]], [2,3,7,11], [1,2,2,2]],
    [[[1,10],[3,3]], [3,3,2], [2,2,1]],
]

run_functional_tests(Solution().fullBloomFlowers, tests)
