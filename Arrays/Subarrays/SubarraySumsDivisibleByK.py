"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.



Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
"""
from typing import List


# Runtime: 340 ms, faster than 20.36% of Python3 online submissions for Subarray Sums Divisible by K.
# Memory Usage: 18.4 MB, less than 35.08% of Python3 online submissions for Subarray Sums Divisible by K.
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        prev = 0
        for i in range(n):
            A[i] += prev
            A[i] %= K
            prev = A[i]
        cnt = 0
        mods = {}
        for i in range(n):
            if A[i] == 0:
                cnt += 1
            cnt1 = mods.get(A[i], 0)
            #cnt2 = mods.get(K - A[i], 0)
            #cnt += cnt1 + cnt2
            cnt += cnt1
            mods[A[i]] = cnt1 + 1
        return cnt


tests = [

    ([-1,2,9], 2, 2),


    ([4,5,0,-2,-3,1], 5, 7)
]

for test in tests:
    result = Solution().subarraysDivByK(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))