"""
https://leetcode.com/problems/greatest-sum-divisible-by-three/

Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.



Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


Constraints:

1 <= nums.length <= 4 * 104
1 <= nums[i] <= 104
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         result = 0
#         r1, r2 = [], []
#         for v in nums:
#             if v % 3 == 0:
#                 result += v
#             elif v % 3 == 1:
#                 r1.append(v)
#             else:
#                 r2.append(v)
#         r1.sort()
#         r2.sort()
#         while r1 and r2:
#             v1, v2 = r1.pop(), r2.pop()
#             result += v1 + v2
#         while len(r1) >= 3:
#             result += r1.pop() + r1.pop() + r1.pop()
#         return result


# WRONG
# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         s = sum(nums)
#         r = s % 3
#         if r == 0:
#             return s
#         h1, h2 = [], []
#         for v in nums:
#             if v % 3 == 1:
#                 heapq.heappush(h1, -v)
#                 if len(h1) > 2:
#                     heapq.heappop(h1)
#             elif v % 3 == 2:
#                 heapq.heappush(h2, -v)
#                 if len(h2) > 2:
#                     heapq.heappop(h2)
#
#         if r == 1:
#             return s - min(-h1[0] if h1 else s, (-h2[0] - h2[1]) if len(h2) >= 2 else s)
#
#         return s - min((-h1[0] - h1[1]) if len(h1) >= 2 else s,
#                        -h2[0] if h2 else s)



# Runtime
# 401 ms
# Beats
# 66.52%
# Memory
# 19.9 MB
# Beats
# 54.19%
# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         s = sum(nums)
#         r = s % 3
#         if r == 0:
#             return s
#         h1, h2 = [], []
#         for v in nums:
#             if v % 3 == 1:
#                 heapq.heappush(h1, v)
#             elif v % 3 == 2:
#                 heapq.heappush(h2, v)
#
#         r11, r12 = heapq.heappop(h1) if h1 else s, heapq.heappop(h1) if h1 else s
#         r21, r22 = heapq.heappop(h2) if h2 else s, heapq.heappop(h2) if h2 else s
#
#         if r == 1:
#             return s - min(r11, r21+r22)
#
#         return s - min(r11 + r12, r21)


# Runtime
# 304 ms
# Beats
# 85.90%
# Memory
# 19.4 MB
# Beats
# 82.38%
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        r = s % 3
        if r == 0:
            return s
        h1, h2 = [], []
        for v in nums:
            if v % 3 == 1:
                if len(h1) < 2:
                    heapq.heappush(h1, -v)
                elif v < -h1[0]:
                    heapq.heappop(h1)
                    heapq.heappush(h1, -v)
            elif v % 3 == 2:
                if len(h2) < 2:
                    heapq.heappush(h2, -v)
                elif v < -h2[0]:
                    heapq.heappop(h2)
                    heapq.heappush(h2, -v)

        r11, r12 = -heapq.heappop(h1) if h1 else s, -heapq.heappop(h1) if h1 else s
        r21, r22 = -heapq.heappop(h2) if h2 else s, -heapq.heappop(h2) if h2 else s

        if r == 1:
            return s - min(r12, r11, r21+r22)

        return s - min(r11 + r12, r22, r21)


tests = [
    [[4,1,5,3,1], 12],
    [[2,6,2,2,7], 15],
    [[3], 3],
    [[3,6,5,1,8], 18],
    [[4], 0],
    [[1,2,3,4,4], 12],
]

run_functional_tests(Solution().maxSumDivThree, tests)
# run_functional_tests(Solution().maxSumDivThree, tests, run_tests=4)
# run_functional_tests(Solution().maxSumDivThree, tests, run_tests=6)
