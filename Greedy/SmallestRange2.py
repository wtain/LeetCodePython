"""
https://leetcode.com/problems/smallest-range-ii/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3573/

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.



Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]


Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

Runtime: 156 ms, faster than 57.06% of Python3 online submissions for Smallest Range II.
Memory Usage: 15.3 MB, less than 86.47% of Python3 online submissions for Smallest Range II.
"""
from typing import List


# class Solution:
#     def smallestRangeII(self, A: List[int], K: int) -> int:
#         ave = sum(A) / len(A)
#         minv = maxv = None
#         for v in A:
#             if v + K <= ave:
#                 v += K
#             else:
#                 v -= K
#             if minv is None:
#                 minv = v
#             else:
#                 minv = min(minv, v)
#             if maxv is None:
#                 maxv = v
#             else:
#                 maxv = max(maxv, v)
#         return maxv - minv

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        result = A[-1] - A[0]
        n = len(A)
        for i in range(n-1):
            a = A[i]
            b = A[i+1]
            high = max(A[n-1] - K, a + K)
            low = min(A[0] + K, b - K)
            result = min(result, high - low)
        return result

tests = [
    ([7,8,8], 5, 1),
    ([1], 0, 0),
    ([0,10], 2, 6),
    ([1,3,6], 3, 3)
]

for test in tests:
    result = Solution().smallestRangeII(test[0], test[1])
    expected = test[2]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))