"""
https://leetcode.com/problems/detonate-the-maximum-bombs/

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.



Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:


Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.


Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 818 ms
# Beats
# 72.13%
# Memory
# 14.2 MB
# Beats
# 87.63%
# class Solution:
#     def maximumDetonation(self, bombs: List[List[int]]) -> int:
#         n = len(bombs)
#         graph = defaultdict(list)
#         for i in range(n):
#             x1, y1, r1 = bombs[i]
#             for j in range(n):
#                 if i == j:
#                     continue
#                 x2, y2, r2 = bombs[j]
#                 if (x2-x1) ** 2 + (y2-y1) ** 2 <= r1**2:
#                     graph[i].append(j)
#
#         def dfs(i0: int) -> int:
#             visited = {i0}
#             to_visit = [i0]
#             result = 0
#             while to_visit:
#                 i = to_visit.pop()
#                 result += 1
#                 for j in graph[i]:
#                     if j not in visited:
#                         visited.add(j)
#                         to_visit.append(j)
#             return result
#
#         return max(map(dfs, range(n)))


# Runtime
# 661 ms
# Beats
# 83.87%
# Memory
# 14.3 MB
# Beats
# 75.99%
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(i+1, n):
                x2, y2, r2 = bombs[j]
                distance2 = (x2-x1) ** 2 + (y2-y1) ** 2
                if distance2 <= r1**2:
                    graph[i].append(j)
                if distance2 <= r2**2:
                    graph[j].append(i)

        def dfs(i0: int) -> int:
            visited = {i0}
            to_visit = [i0]
            result = 0
            while to_visit:
                i = to_visit.pop()
                result += 1
                for j in graph[i]:
                    if j not in visited:
                        visited.add(j)
                        to_visit.append(j)
            return result

        return max(map(dfs, range(n)))


tests = [
    [[[2,1,3],[6,1,4]], 2],
    [[[1,1,5],[10,10,5]], 1],
    [[[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]], 5],
]

run_functional_tests(Solution().maximumDetonation, tests)
