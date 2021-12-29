"""
https://leetcode.com/problems/interval-list-intersections/

You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].



Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
Example 3:

Input: firstList = [], secondList = [[4,8],[10,12]]
Output: []
Example 4:

Input: firstList = [[1,7]], secondList = [[3,10]]
Output: [[3,7]]


Constraints:

0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Ma
# https://leetcode.com/submissions/detail/343443419/
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        n1, n2 = len(firstList), len(secondList)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            low = max(firstList[i1][0], secondList[i2][0])
            high = min(firstList[i1][1], secondList[i2][1])
            if low <= high:
                result.append([low, high])
            if firstList[i1][1] < secondList[i2][1]:
                i1 += 1
            else:
                i2 += 1
        return result


tests = [
    [[[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]], [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]],
    [[[1,3],[5,9]], [], []],
    [[], [[4,8],[10,12]], []],
    [[[1,7]], [[3,10]], [[3,7]]]
]


run_functional_tests(Solution().intervalIntersection, tests)
