"""
https://leetcode.com/problems/max-chunks-to-make-sorted/

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.



Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.


Constraints:

n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         result1 = 0
#         i, n = 0, len(arr)
#         while i < n:
#             while arr[i] > i:
#                 i = max(i, arr[i])
#             i += 1
#             result1 += 1
#         i = n-1
#         result2 = 0
#         while i >= 0:
#             while arr[i] < i:
#                 i = min(i, arr[i])
#             i -= 1
#             result2 += 1
#         return min(result1, result2)


# Runtime: 66 ms, faster than 6.40% of Python3 online submissions for Max Chunks To Make Sorted.
# Memory Usage: 13.9 MB, less than 57.60% of Python3 online submissions for Max Chunks To Make Sorted.
# https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/2000522/Java-oror-Iterative-oror-Easy-oror-0ms-100-Beat
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n, result = len(arr), 0
        mx = 0
        for i in range(n):
            mx = max(mx, arr[i])
            if mx == i:
                result += 1
        return result


tests = [
    [[4,3,2,1,0], 1],
    [[1,0,2,3,4], 4],
    [[1,2,0,3], 2],
    [[1,4,0,2,3,5], 2],
    [[0,4,5,2,1,3], 2]
]

run_functional_tests(Solution().maxChunksToSorted, tests)
