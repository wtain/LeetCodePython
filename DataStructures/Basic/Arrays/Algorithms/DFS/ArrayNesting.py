"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3960/
https://leetcode.com/problems/array-nesting/

You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].



Example 1:

Input: nums = [5,4,0,3,1,6,2]
Output: 4
Explanation:
nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
One of the longest sets s[k]:
s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
Example 2:

Input: nums = [0,1,2]
Output: 1


Constraints:

1 <= nums.length <= 105
0 <= nums[i] < nums.length
All the values of nums are unique.
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_l = 0
#
#         for k in range(n):
#             visited = set()
#             v, l = nums[k], 0
#             while v not in visited:
#                 visited.add(v)
#                 v = nums[v]
#                 l += 1
#             max_l = max(max_l, l)
#
#         return max_l


# Runtime: 204 ms, faster than 11.06% of Python3 online submissions for Array Nesting.
# Memory Usage: 36.2 MB, less than 5.09% of Python3 online submissions for Array Nesting.
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_l = 0
#
#         cache = dict()
#
#         def dfs(k: int) -> int:
#             # print(nums[k], end='')
#
#             if k in cache:
#                 return cache[k]
#
#             v, l = nums[k], 0
#             if v in visited:
#                 return 0
#             visited.add(v)
#             result = 1 + dfs(v)
#             cache[k] = result
#             return result
#
#         for k in range(n):
#             visited = set()
#             l = dfs(k)
#             # print()
#             max_l = max(max_l, l)
#
#         return max_l


# Runtime: 178 ms, faster than 14.38% of Python3 online submissions for Array Nesting.
# Memory Usage: 19 MB, less than 40.71% of Python3 online submissions for Array Nesting.
# class Solution:
#     def arrayNesting(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_l = 0
#
#         visited = set()
#
#         def dfs(k: int) -> int:
#             l = 0
#             while k not in visited:
#                 visited.add(k)
#                 l += 1
#                 k = nums[k]
#             return l
#
#         for k in range(n):
#             l = dfs(k)
#             max_l = max(max_l, l)
#
#         return max_l


# Runtime: 175 ms, faster than 14.82% of Python3 online submissions for Array Nesting.
# Memory Usage: 16.6 MB, less than 70.35% of Python3 online submissions for Array Nesting.
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        max_l = 0

        def dfs(k: int) -> int:
            l = 0
            while nums[k] < n:
                new_k = nums[k]
                nums[k] += n
                l += 1
                k = new_k
            return l

        for k in range(n):
            l = dfs(k)
            max_l = max(max_l, l)

        return max_l



tests = [
    [[5,4,0,3,1,6,2], 4],
    [[0,1,2], 1]
]

run_functional_tests(Solution().arrayNesting, tests)