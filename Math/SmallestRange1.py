"""
https://leetcode.com/problems/smallest-range-i/
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

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
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]


Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

Runtime: 108 ms, faster than 82.13% of Python3 online submissions for Smallest Range I.
Memory Usage: 15.3 MB, less than 82.13% of Python3 online submissions for Smallest Range I.

Runtime: 108 ms, faster than 82.13% of Python3 online submissions for Smallest Range I.
Memory Usage: 15.3 MB, less than 82.13% of Python3 online submissions for Smallest Range I.
"""
from typing import List


# class Solution:
#     def smallestRangeI(self, A: List[int], K: int) -> int:
#         A = sorted(A)
#         n = len(A)
#         v_min = A[0]
#         v_max = A[-1]
#         result = max(v_max - v_min - 2 * K, 0)
#         return result

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        v_min = min(A)
        v_max = max(A)
        result = max(v_max - v_min - 2 * K, 0)
        return result


tests = [
    ([1], 0, 0),
    ([0,10], 2, 6),
    ([1,3,6], 3, 0)
]

for test in tests:
    result = Solution().smallestRangeI(test[0], test[1])
    expected = test[2]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))