"""
https://leetcode.com/problems/longest-turbulent-subarray/

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.


Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1


Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
"""
from typing import List


# Runtime: 508 ms, faster than 58.64% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 18.8 MB, less than 26.85% of Python3 online submissions for Longest Turbulent Subarray.
# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         n = len(arr)
#         if n < 2:
#             return n
#         max_len = curr_len = 2 if arr[0] != arr[1] else 1
#         for i in range(2, n):
#             if arr[i-2] < arr[i-1] and arr[i] < arr[i-1]:
#                 curr_len += 1
#             elif arr[i-2] > arr[i-1] and arr[i] > arr[i-1]:
#                 curr_len += 1
#             elif arr[i] == arr[i - 1]:
#                 curr_len = 1
#             else:
#                 curr_len = 2
#             max_len = max(max_len, curr_len)
#         return max_len


# Runtime: 540 ms, faster than 34.98% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 18.6 MB, less than 69.23% of Python3 online submissions for Longest Turbulent Subarray.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        def cmp(a, b: int) -> int:
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

        n = len(arr)
        result = 1

        start = 0
        for i in range(1, n):
            sign = cmp(arr[i-1], arr[i])
            if sign == 0:
                start = i
            elif i == n-1 or sign * cmp(arr[i], arr[i+1]) != -1:
                result = max(result, i - start + 1)
                start = i

        return result


tests = [
    ([37,199,60,296,257,248,115,31,273,176], 5),

    ([9,9], 1),

    ([9,4,2,10,7,8,8,1,9], 5),
    ([4,8,12,16], 2),
    ([100], 1)
]

run_functional_tests(Solution().maxTurbulenceSize, tests)
