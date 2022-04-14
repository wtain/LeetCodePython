"""
https://leetcode.com/problems/split-array-largest-sum/

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
"""
from functools import lru_cache
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# https://leetcode.com/problems/split-array-largest-sum/solution/
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         prefix_sums = [0] + list(accumulate(nums))
#
#         @lru_cache(None)
#         def get_min_largest_split_sum(current_index: int, subarray_count: int):
#             if subarray_count == 1:
#                 return prefix_sums[n] - prefix_sums[current_index]
#
#             minimum_largest_split_sum = prefix_sums[n]
#             for i in range(n - subarray_count + 1):
#                 first_split_sum = prefix_sums[i + 1] - prefix_sums[current_index]
#                 largest_split_sum = max(first_split_sum,
#                                         get_min_largest_split_sum(i+1, subarray_count-1))
#                 minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)
#                 if first_split_sum >= minimum_largest_split_sum:
#                     break
#
#             return minimum_largest_split_sum
#
#         return get_min_largest_split_sum(0, m)


# TLE
# https://leetcode.com/problems/split-array-largest-sum/solution/
# class Solution:
#     def splitArray(self, nums: List[int], m: int) -> int:
#         n = len(nums)
#         memo = [[0] * (m+1) for _ in range(n)]
#
#         prefix_sums = [0] + list(accumulate(nums))
#
#         for subarray_count in range(1, m+1):
#             for curr_index in range(n):
#                 if subarray_count == 1:
#                     memo[curr_index][subarray_count] = prefix_sums[n] - prefix_sums[curr_index]
#                     continue
#
#                 minimum_largest_split_sum = prefix_sums[n]
#                 for i in range(n - subarray_count + 1):
#                     first_split_sum = prefix_sums[i + 1] - prefix_sums[curr_index]
#                     largest_split_sum = max(first_split_sum,
#                                             memo[i+1][subarray_count-1])
#                     minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)
#                     if first_split_sum >= minimum_largest_split_sum:
#                         break
#
#                 memo[curr_index][subarray_count] = minimum_largest_split_sum
#
#         return memo[0][m]


# Runtime: 57 ms, faster than 54.20% of Python3 online submissions for Split Array Largest Sum.
# Memory Usage: 13.8 MB, less than 96.00% of Python3 online submissions for Split Array Largest Sum.
# https://leetcode.com/problems/split-array-largest-sum/solution/
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum, splits_required = 0, 0

            for el in nums:
                if current_sum + el <= max_sum_allowed:
                    current_sum += el
                else:
                    current_sum = el
                    splits_required += 1

            return splits_required + 1

        left, right = max(nums), sum(nums)
        while left <= right:
            max_sum_allowed = (left + right) // 2
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                min_largest_split_sum = max_sum_allowed
            else:
                left = max_sum_allowed + 1

        return min_largest_split_sum



tests = [
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,350,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,450,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,500,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,550,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,600,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,650,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,700,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,750,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,800,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,850,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,900,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,950,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],50,950],

    [[7,2,5,10,8], 2, 18],
    [[1,2,3,4,5], 2, 9],
    [[1,4,4], 3, 4]
]

run_functional_tests(Solution().splitArray, tests)
