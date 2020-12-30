"""
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.



Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even

Runtime: 200 ms, faster than 66.80% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.8 MB, less than 10.16% of Python3 online submissions for N-Repeated Element in Size 2N Array.

Runtime: 192 ms, faster than 88.90% of Python3 online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 15.7 MB, less than 23.86% of Python3 online submissions for N-Repeated Element in Size 2N Array.
"""
from typing import List


# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:
#         M = len(A)
#         N = M >> 1
#         S = sum(A)
#         S1 = N * (N+1) >> 1
#         print(str(S1) + " " + str(S))
#         return int((S - S1) / N)

# class Solution:
#     def repeatedNTimes(self, A: List[int]) -> int:
#         counts = {}
#         for a in A:
#             counts[a] = counts.get(a, 0) + 1
#             if counts[a] > 1:
#                 return a

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        n = len(A)
        for k in range(1, 4):
            for i in range(n - k):
                if A[i] == A[i+k]:
                    return A[i]


tests: List = [
    ([1,2,3,3], 3),
    ([2,1,2,5,3,2], 2),
    ([5,1,5,2,5,3,5,4], 5)
]

for test in tests:
    result = Solution().repeatedNTimes(test[0])
    if test[1] == result:
        print("PASS")
    else:
        print("FAIL")