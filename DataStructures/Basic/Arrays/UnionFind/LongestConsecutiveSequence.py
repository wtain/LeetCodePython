"""
https://leetcode.com/problems/longest-consecutive-sequence/
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3769/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 356 ms, faster than 23.38% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 41 MB, less than 5.03% of Python3 online submissions for Longest Consecutive Sequence.
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         numbers = set(nums)
#         n = len(numbers)
#         p, r, w = [0] * n, [0] * n, [1] * n
#         for i in range(n):
#             p[i] = i
#
#         def find_set(x: int) -> int:
#             nonlocal p, r
#             while p[x] != x:
#                 x = p[x]
#             return x
#
#         def union(x: int, y: int):
#             nonlocal p, r, w
#             if p[x] == p[y]:
#                 return
#
#             if r[x] > r[y]:
#                 p[y] = x
#                 w[x] += w[y]
#             else:
#                 p[x] = y
#                 w[y] += w[x]
#                 if r[x] == r[y]:
#                     r[y] += 1
#
#         numbers = dict((x, i) for i, x in enumerate(numbers))
#
#         for x in numbers:
#             for y in [x-1, x+1]:
#                 if y in numbers:
#                     union(find_set(numbers[x]), find_set(numbers[y]))
#
#         return max(w)


# Runtime: 180 ms, faster than 41.47% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 25.7 MB, less than 24.14% of Python3 online submissions for Longest Consecutive Sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        numbers = set(nums)
        for x in numbers:
            if x-1 not in numbers:
                current = x
                current_streak = 1
                while current+1 in numbers:
                    current += 1
                    current_streak += 1
                result = max(result, current_streak)
        return result


tests = [
    [[1,3,5,2,4], 5],
    [[], 0],
    [[100,4,200,1,3,2], 4],
    [[0,3,7,2,5,8,4,6,0,1], 9]
]

run_functional_tests(Solution().longestConsecutive, tests)