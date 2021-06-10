"""
https://leetcode.com/problems/count-good-triplets/

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.



Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.


Constraints:

3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
"""
import itertools
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1560 ms, faster than 6.86% of Python3 online submissions for Count Good Triplets.
# Memory Usage: 14.3 MB, less than 33.33% of Python3 online submissions for Count Good Triplets.
# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         n = len(arr)
#         cnt = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     d1 = abs(arr[i] - arr[j])
#                     d2 = abs(arr[j] - arr[k])
#                     d3 = abs(arr[i] - arr[k])
#                     if d1 <= a and d2 <= b and d3 <= c:
#                         cnt += 1
#         return cnt


# Runtime: 684 ms, faster than 52.77% of Python3 online submissions for Count Good Triplets.
# Memory Usage: 14.2 MB, less than 61.19% of Python3 online submissions for Count Good Triplets.
# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         n = len(arr)
#         cnt = 0
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 for k in range(j+1, n):
#                     if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                         cnt += 1
#         return cnt

# Runtime: 540 ms, faster than 68.80% of Python3 online submissions for Count Good Triplets.
# Memory Usage: 14.2 MB, less than 61.19% of Python3 online submissions for Count Good Triplets.
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        return sum(1 for a1, a2, a3 in itertools.combinations(arr, 3) if abs(a1-a2) <= a and abs(a2-a3) <= b and abs(a1-a3) <= c)


tests = [
    [[3,0,1,1,9,7], 7, 2, 3, 4],
    [[1,1,2,2,3], 0, 0, 1, 0]
]

run_functional_tests(Solution().countGoodTriplets, tests)