"""
https://leetcode.com/problems/longest-mountain-in-array/

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.



Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104


Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 174 ms
# Beats
# 87.13%
# Memory
# 15.2 MB
# Beats
# 39.13%
# class Solution:
#     def longestMountain(self, arr: List[int]) -> int:
#         n = len(arr)
#         num_less = [1] * n
#         num_greater = [1] * n
#         for i in range(1, n):
#             if arr[i] > arr[i-1]:
#                 num_less[i] = num_less[i-1] + 1
#         for i in range(n-2, -1, -1):
#             if arr[i] > arr[i+1]:
#                 num_greater[i] = num_greater[i+1] + 1
#         return max(less + greater - 1 if less > 1 and greater > 1 else 0 for less, greater in zip(num_less, num_greater))


# Runtime
# 184 ms
# Beats
# 72.13%
# Memory
# 15.2 MB
# Beats
# 39.13%
# https://leetcode.com/problems/longest-mountain-in-array/solutions/136806/longest-mountain-in-array/
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = base = 0
        while base < n:
            end = base
            if end+1 < n and arr[end] < arr[end+1]:
                while end+1 < n and arr[end] < arr[end+1]:
                    end += 1
                if end+1 < n and arr[end] > arr[end+1]:
                    while end+1 < n and arr[end] > arr[end+1]:
                        end += 1
                    result = max(result, end-base+1)
            base = max(end, base+1)
        return result


tests = [
    [[2,1,4,7,3,2,5], 5],
    [[2,2,2], 0],
]

run_functional_tests(Solution().longestMountain, tests)
