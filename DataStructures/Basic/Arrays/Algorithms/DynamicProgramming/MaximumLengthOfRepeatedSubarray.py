"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3807/
https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.



Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 6012 ms, faster than 12.57% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 14.6 MB, less than 86.08% of Python3 online submissions for Maximum Length of Repeated Subarray.
# class Solution:
#     def findLength(self, nums1: List[int], nums2: List[int]) -> int:
#         n1, n2, m = len(nums1), len(nums2), 0
#         if n2 > n1:
#             return self.findLength(nums2, nums1)
#         dp = [[0] * (n2+1) for _ in range(2)]
#         for i in range(n1+1):
#             i1 = i % 2
#             i2 = 1 - i1
#             for j in range(n2+1):
#                 if i == 0 or j == 0:
#                     dp[i1][j] = 0
#                 elif nums1[i - 1] == nums2[j - 1]:
#                     dp[i1][j] = dp[i2][j-1] + 1
#                 else:
#                     dp[i1][j] = 0
#                 m = max(m, dp[i1][j])
#         return m


# Runtime: 312 ms, faster than 97.32% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 14.6 MB, less than 86.08% of Python3 online submissions for Maximum Length of Repeated Subarray.
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/solution/
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        P, MOD = 113, 10**9 + 7
        Pinv = pow(P, MOD - 2, MOD)

        def check(guess):
            def rolling(A, length):
                if length == 0:
                    yield 0, 0
                    return

                h, power = 0, 1
                for i, x in enumerate(A):
                    h = (h + x * power) % MOD
                    if i < length - 1:
                        power = (power * P) % MOD
                    else:
                        yield h, i - (length - 1)
                        h = (h - A[i - (length - 1)]) * Pinv % MOD

            hashes = defaultdict(list)
            for ha, start in rolling(nums1, guess):
                hashes[ha].append(start)
            for ha, start in rolling(nums2, guess):
                iarr = hashes.get(ha, [])
                if any(nums1[i: i+guess] == nums2[start: start+guess] for i in iarr):
                    return True
            return False

        lo, hi = 0, min(len(nums1), len(nums2))+1
        while lo < hi:
            mi = lo + (hi-lo) // 2
            if check(mi):
                lo = mi+1
            else:
                hi = mi
        return lo-1


tests = [
    [[1,2,3,2,1], [3,2,1,4,7], 3],
    [[0,0,0,0,0], [0,0,0,0,0], 5]
]

run_functional_tests(Solution().findLength, tests)