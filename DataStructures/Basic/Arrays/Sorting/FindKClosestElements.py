"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3800/
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b


Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 288 ms, faster than 75.04% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.6 MB, less than 40.37% of Python3 online submissions for Find K Closest Elements.
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         n = len(arr)
#         f = bisect.bisect_left(arr, x)
#         i1 = f - 1
#         i2 = i1 + 1
#         for i in range(k):
#             d1 = (x - arr[i1]) if i1 >= 0 else math.inf
#             d2 = (arr[i2] - x) if i2 < n else math.inf
#             if d1 <= d2:
#                 i1 -= 1
#             else:
#                 i2 += 1
#         return arr[i1+1:i2]


# Runtime: 280 ms, faster than 85.40% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 15.6 MB, less than 69.77% of Python3 online submissions for Find K Closest Elements.
# https://leetcode.com/problems/find-k-closest-elements/solution/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            mid = l + (r-l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]


tests = [
    [[1,2,3,4,5], 4, 3, [1,2,3,4]],
    [[1,2,3,4,5], 4, -1, [1,2,3,4]]
]

run_functional_tests(Solution().findClosestElements, tests)