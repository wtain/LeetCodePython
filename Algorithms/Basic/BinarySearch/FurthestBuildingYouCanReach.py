"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3721/
https://leetcode.com/problems/furthest-building-you-can-reach/

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.



Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3


Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length

Assume the problem is to check whether you can reach the last building or not.
You'll have to do a set of jumps, and choose for each one whether to do it using a rope or bricks. It's always optimal to use ropes in the largest jumps.
Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far, and stop whenever this sum exceeds b.
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2120 ms, faster than 5.74% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 28.8 MB, less than 37.16% of Python3 online submissions for Furthest Building You Can Reach.
# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#
#         def can_reach(index: int) -> bool:
#             max_h = []
#             low_jumps = 0
#             for i in range(1, index+1):
#                 if heights[i] <= heights[i-1]:
#                     continue
#                 dh = heights[i] - heights[i-1]
#                 heapq.heappush(max_h, dh)
#                 if len(max_h) > ladders:
#                     v = heapq.heappop(max_h)
#                     low_jumps += v
#                     if low_jumps > bricks:
#                         return False
#             return True
#
#         l, r = 0, len(heights)
#         while l < r:
#             m = l + (r-l) // 2
#             if can_reach(m):
#                 l = m+1
#             else:
#                 r = m
#
#         return l-1


# https://leetcode.com/problems/furthest-building-you-can-reach/discuss/1177219/Python-Solution-using-binary-search-explained
# Runtime: 1168 ms, faster than 12.12% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 28.1 MB, less than 99.36% of Python3 online submissions for Furthest Building You Can Reach.
# class Solution:
#     def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#
#         heights += [float("inf")]
#
#         def can_reach(index: int) -> bool:
#             to_climb = [y - x for y, x in zip(heights[1:index+1], heights[:index+1]) if y > x]
#             return len(to_climb) <= ladders or sum(sorted(to_climb)[::-1][ladders:]) <= bricks
#
#         l, r = 0, len(heights)-1
#         while l+1 < r:
#             m = l + (r-l) // 2
#             if can_reach(m):
#                 l = m
#             else:
#                 r = m
#
#         return l


# https://leetcode.com/problems/furthest-building-you-can-reach/discuss/1177243/JS-Python-Java-C%2B%2B-or-Easy-Min-Heap-Solution-w-Explanation
# Runtime: 564 ms, faster than 93.30% of Python3 online submissions for Furthest Building You Can Reach.
# Memory Usage: 28.8 MB, less than 37.16% of Python3 online submissions for Furthest Building You Can Reach.
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        h = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heapq.heappush(h, diff)
                    ladders -= 1
                elif h and diff > h[0]:
                    heapq.heappush(h, diff)
                    bricks -= heapq.heappop(h)
                else:
                    bricks -= diff
                if bricks < 0:
                    return i
        return len(heights) - 1


tests = [
    [[4,2,7,6,9,14,12], 5, 1, 4],
    [[4,12,2,7,3,18,20,3,19], 10, 2, 7],
    [[14,3,19,3], 17, 0, 3]
]

run_functional_tests(Solution().furthestBuilding, tests)