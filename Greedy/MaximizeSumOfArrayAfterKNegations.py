"""
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)

Return the largest possible sum of the array after modifying it in this way.



Example 1:

Input: A = [4,2,3], K = 1
Output: 5
Explanation: Choose indices (1,) and A becomes [4,-2,3].
Example 2:

Input: A = [3,-1,0,2], K = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
Example 3:

Input: A = [2,-3,-1,5,-4], K = 2
Output: 13
Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].


Note:

1 <= A.length <= 10000
1 <= K <= 10000
-100 <= A[i] <= 100
"""
from typing import List


# Runtime: 48 ms, faster than 65.66% of Python3 online submissions for Maximize Sum Of Array After K Negations.
# Memory Usage: 14.5 MB, less than 28.11% of Python3 online submissions for Maximize Sum Of Array After K Negations.
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        n = len(A)
        zeros = A.count(0)
        negative = sum(1 if x < 0 else 0 for x in A)
        positive = n - negative - zeros
        A = sorted(A)
        i = 0
        while K > 0 and i < n and A[i] < 0:
            A[i] = -A[i]
            i += 1
            K -= 1
        if zeros > 0:
            K = 0
        else:
            K = K % 2
            res = sum(A)
            if K:
                res -= 2 * min(A)
            return res

        return sum(A)


tests = [
    ([-2,9,9,8,4], 5, 32),

    ([4,2,3], 1, 5),
    ([3,-1,0,2], 3, 6),
    ([2,-3,-1,5,-4], 2, 13)
]

for test in tests:
    result = Solution().largestSumAfterKNegations(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))