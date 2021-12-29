"""
https://leetcode.com/problems/minimum-absolute-difference/

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 404 ms, faster than 29.93% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 32.7 MB, less than 15.71% of Python3 online submissions for Minimum Absolute Difference.
# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arr.sort()
#         diffs = sorted([(v2-v1,v1,v2) for v1, v2 in zip(arr, arr[1:])])
#         i = 1
#         while i < len(diffs) and diffs[i][0] == diffs[i-1][0]:
#             i += 1
#         return [[v1, v2] for d,v1,v2 in diffs[:i]]


# Runtime: 324 ms, faster than 89.20% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 28.2 MB, less than 24.57% of Python3 online submissions for Minimum Absolute Difference.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_diff = arr[1] - arr[0]
        n = len(arr)
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            if diff > min_diff:
                continue
            if diff < min_diff:
                result = []
                min_diff = diff
            result.append([arr[i-1], arr[i]])
        return result


tests = [
    [[4,2,1,3], [[1,2],[2,3],[3,4]]],
    [[1,3,6,10,15], [[1,3]]],
    [[3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]]
]

run_functional_tests(Solution().minimumAbsDifference, tests)
