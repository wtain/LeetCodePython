"""
https://leetcode.com/problems/number-of-boomerangs/
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
from typing import List, Dict

""" Naive, TLE? """
"""
class Solution:

    def dist2(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        cnt = 1
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.dist2(points[i], points[j]) == self.dist2(points[j], points[k]):
                        cnt += 1
                    if self.dist2(points[i], points[k]) == self.dist2(points[k], points[j]):
                        cnt += 1
                    if self.dist2(points[k], points[i]) == self.dist2(points[i], points[j]):
                        cnt += 1
        return cnt
"""

"""
Runtime: 940 ms, faster than 90.42% of Python3 online submissions for Number of Boomerangs.
Memory Usage: 26.9 MB, less than 20.64% of Python3 online submissions for Number of Boomerangs.
"""
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        distcounts: List[Dict[int, int]] = [{} for i in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                d = dx ** 2 + dy ** 2

                distcounts[i][d] = (distcounts[i].get(d) or 0) + 1
                distcounts[j][d] = (distcounts[j].get(d) or 0) + 1
        cnt = 0
        for i in range(n):
            for d in distcounts[i]:
                c = distcounts[i][d]
                if c < 2:
                    continue
                cnt += (c-1) * c
        return cnt


print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))  # 2
