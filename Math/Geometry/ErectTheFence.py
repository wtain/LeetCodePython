"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3962/
https://leetcode.com/problems/erect-the-fence/

You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.



Example 1:


Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
Example 2:


Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]


Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.
"""
import functools
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.ResultComparators import compareSets


# https://leetcode.com/problems/erect-the-fence/solution/
# Runtime: 1456 ms, faster than 5.81% of Python3 online submissions for Erect the Fence.
# Memory Usage: 15.1 MB, less than 51.16% of Python3 online submissions for Erect the Fence.
class Solution:

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        n = len(trees)
        if n < 4:
            return trees

        def orientation(p, q, r) -> int:
            return (q[1] - p[1]) * (r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])

        def in_between(p, i, q) -> bool:
            return (p[0] <= i[0] <= q[0] or q[0] <= i[0] <= p[0]) and \
                   (p[1] <= i[1] <= q[1] or q[1] <= i[1] <= p[1])

        left_most = 0
        for i in range(n):
            if trees[i][0] < trees[left_most][0]:
                left_most = i

        q = -1
        hull = set()
        p = left_most
        while q != left_most:
            q = (p+1) % n
            for i in range(n):
                if orientation(trees[p], trees[i], trees[q]) < 0:
                    q = i

            for i in range(n):
                if i != p and i != q and \
                        orientation(trees[p], trees[i], trees[q]) == 0 and \
                        in_between(trees[p], trees[i], trees[q]):
                    hull.add((trees[i][0], trees[i][1]))

            hull.add((trees[q][0], trees[q][1]))
            p = q

        return [[p[0], p[1]] for p in {(p[0], p[1]) for p in hull}]


# Runtime: 864 ms, faster than 5.81% of Python3 online submissions for Erect the Fence.
# Memory Usage: 15 MB, less than 51.16% of Python3 online submissions for Erect the Fence.
# https://leetcode.com/problems/erect-the-fence/solution/
# class Solution:
#
#     def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
#
#         n = len(trees)
#         if n < 4:
#             return trees
#
#         def orientation(p, q, r) -> int:
#             return (q[1] - p[1]) * (r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
#
#         def distance(p, q) -> int:
#             return (p[0] - q[0]) ** 2 + (p[1]-q[1]) ** 2
#
#         def bottom_left(trees):
#             res = trees[0]
#             for p in trees:
#                 if p[1] < res[1]:
#                     res = p
#             return res
#
#         def compare(p, q):
#             diff = orientation(bm, p, q) - orientation(bm, q, p)
#             if diff == 0:
#                 return distance(bm, p) - distance(bm, q)
#             elif diff > 0:
#                 return 1
#             else:
#                 return -1
#
#         bm = bottom_left(trees)
#         trees.sort(key=functools.cmp_to_key(compare))
#         i = n - 1
#         while i >= 0 and orientation(bm, trees[-1], trees[i]) == 0:
#             i -= 1
#         l, h = i+1, n-1
#         while l < h:
#             trees[l], trees[h] = trees[h], trees[l]
#             l += 1
#             h -= 1
#
#         st = [trees[0], trees[1]]
#         for j in range(2, n):
#             top = st.pop()
#             while orientation(st[-1], top, trees[j]) > 0:
#                 top = st.pop()
#             st.append(top)
#             st.append(trees[j])
#         return st


# Runtime: 408 ms, faster than 17.44% of Python3 online submissions for Erect the Fence.
# Memory Usage: 14.9 MB, less than 76.74% of Python3 online submissions for Erect the Fence.
# https://leetcode.com/problems/erect-the-fence/solution/
# class Solution:
#
#     def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
#
#         n = len(trees)
#         if n < 4:
#             return trees
#
#         def orientation(p, q, r) -> int:
#             return (q[1] - p[1]) * (r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
#
#         trees.sort()
#         hull = []
#         for i in range(n):
#             while len(hull) >= 2 and orientation(hull[-2], hull[-1], trees[i]) > 0:
#                 hull.pop()
#             hull.append(trees[i])
#         hull.pop()
#         for i in range(n-1, -1, -1):
#             while len(hull) >= 2 and orientation(hull[-2], hull[-1], trees[i]) > 0:
#                 hull.pop()
#             hull.append(trees[i])
#         return [[p[0], p[1]] for p in {(p[0], p[1]) for p in hull}]


tests = [
    [[[1,2],[2,2],[4,2],[5,2],[6,2],[7,2]], [[7,2],[5,2],[6,2],[1,2],[2,2],[4,2]]],

    [[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]], [[1,1],[2,0],[3,3],[2,4],[4,2]]],
    [[[1,2],[2,2],[4,2]], [[4,2],[2,2],[1,2]]]
]

run_functional_tests(Solution().outerTrees, tests, custom_check=compareSets)