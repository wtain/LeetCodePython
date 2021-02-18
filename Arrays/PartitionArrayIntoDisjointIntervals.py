"""
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.
"""
from typing import List


# Runtime: 228 ms, faster than 33.55% of Python3 online submissions for Partition Array into Disjoint Intervals.
# Memory Usage: 18.4 MB, less than 70.65% of Python3 online submissions for Partition Array into Disjoint Intervals.
# class Solution:
#     def partitionDisjoint(self, A: List[int]) -> int:
#
#         # max(left) < min(right)
#         n = len(A)
#         rmins = [0] * n
#         lmaxs = [0] * n
#
#         rmins[-1] = A[-1]
#         lmaxs[0] = A[0]
#         for i in range(1, n):
#             lmaxs[i] = max(A[i], lmaxs[i-1])
#             rmins[-i-1] = min(A[-i-1], rmins[-i])
#
#         i = 0
#         while i < n-1 and lmaxs[i] > rmins[i+1]:
#             i += 1
#
#         return i + 1

# Runtime: 208 ms, faster than 51.61% of Python3 online submissions for Partition Array into Disjoint Intervals.
# Memory Usage: 18.3 MB, less than 70.65% of Python3 online submissions for Partition Array into Disjoint Intervals.
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:

        # max(left) < min(right)
        n = len(A)
        rmins = [0] * n

        rmins[-1] = A[-1]
        for i in range(1, n):
            rmins[-i-1] = min(A[-i-1], rmins[-i])

        i = 0
        mx = A[0]
        while i < n-1 and mx > rmins[i+1]:
            i += 1
            mx = max(mx, A[i])

        return i + 1



tests = [
    ([5,0,3,8,6], 3),
    ([1,1,1,0,6,12], 4)
]

for test in tests:
    result = Solution().partitionDisjoint(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))