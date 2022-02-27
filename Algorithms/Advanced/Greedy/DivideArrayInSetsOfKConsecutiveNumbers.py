"""
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if it is possible. Otherwise, return False.



Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 109


Note: This question is the same as 846: https://leetcode.com/problems/hand-of-straights/
"""
from collections import Counter
from typing import List


# TLE
# class Solution:
#     def isPossibleDivide(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         if n % k:
#             return False
#         m = n // k
#         nums.sort()
#
#         used = [False] * n
#
#         def fetch_next(j: int, prev) -> int:
#             nonlocal used, n, nums
#             # while j < n and ((not prev or nums[j] == prev) or used[j]):
#             if prev:
#                 while j < n and nums[j] == prev:
#                     j += 1
#             while j < n and used[j]:
#                 j += 1
#             return j
#
#         # groups = [[] for _ in range(m)]
#         for i in range(m):
#             prev = None
#             j = 0
#             for _ in range(k):
#                 j = fetch_next(j, prev)
#                 if j == n:
#                     return False
#                 if prev and nums[j] != prev+1:
#                     return False
#                 # groups[i].append(nums[j])
#                 prev = nums[j]
#                 used[j] = True
#                 j += 1
#         return True

# Runtime: 408 ms, faster than 79.89% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
# Memory Usage: 28.8 MB, less than 34.62% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
# Runtime: 400 ms, faster than 89.80% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
# Memory Usage: 28.9 MB, less than 34.62% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k:
            return False
        m = n // k

        c = Counter(nums)
        nums_sorted = sorted(c.keys())
        ni = 0

        for i in range(m):
            prev = None
            for _ in range(k):
                if prev is not None:
                    if not c[prev+1]:
                        return False
                    c[prev+1] -= 1
                    prev += 1
                else:
                    while ni < len(nums_sorted) and not c[nums_sorted[ni]]:
                        ni += 1
                    if ni == len(nums_sorted):
                        return False
                    prev = nums_sorted[ni]
                    c[prev] -= 1
                    if not c[prev]:
                        ni += 1
        return True


tests = [
    [[1,2,3,3,4,4,5,6], 4, True],
    [[3,2,1,2,3,4,3,4,5,9,10,11], 3, True],
    [[3,3,2,2,1,1], 3, True],
    [[1,2,3,4], 3, False]
]

run_functional_tests(Solution().isPossibleDivide, tests)
