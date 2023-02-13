"""
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.


Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
#         n = len(arr)
#         st = []
#         for i in range(n):
#             while st and arr[st[-1]] > arr[i]:
#                 st.pop()
#             st.append(i)
#         return n - len(st)

# Runtime
# 665 ms
# Beats
# 66.40%
# Memory
# 28.7 MB
# Beats
# 63.16%
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/solutions/3153397/java-solution-1-ms-beats-100/
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        while i < n-1 and arr[i] <= arr[i+1]:
            i += 1
        if i == n-1:
            return 0
        j = n-1
        while j > 0 and arr[j] >= arr[j-1]:
            j -= 1
        min_len = min(n - i - 1, j)
        while i >= 0:
            for k in range(j, n):
                if arr[i] > arr[k]:
                    continue
                min_len = min(min_len, k - i - 1)
                break
            i -= 1
        return min_len


tests = [
    [[1,2,3,10,4,1,3,5], 3],
    [[1,2,3,10,4,2,3,5], 3],
    [[5,4,3,2,1], 4],
    [[1,2,3], 0],
]

run_functional_tests(Solution().findLengthOfShortestSubarray, tests)
