"""
https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.



Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].


Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 9859
# ms
# Beats
# 5.07%
# of users with Python3
# Memory
# 16.44
# MB
# Beats
# 96.46%
# of users with Python3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#
#         def impl(index, mask):
#             if index == len(nums):
#                 return 1 if mask > 0 else 0
#
#             is_beautiful = True
#
#             for j in range(index):
#                 if ((1 << j) & mask) == 0 or abs(nums[j] - nums[index]) != k:
#                     continue
#                 else:
#                     is_beautiful = False
#                     break
#
#             skip = impl(index+1, mask)
#             take = (impl(index+1, mask | (1 << index)) if is_beautiful else 0)
#
#             return skip + take
#
#         return impl(0, 0)


# Runtime
# 3007
# ms
# Beats
# 41.49%
# of users with Python3
# Memory
# 16.61
# MB
# Beats
# 53.29%
# of users with Python3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#
#         freq_map = defaultdict(int)
#         nums.sort()
#
#         def impl(i):
#             if i == len(nums):
#                 return 1
#
#             total_count = impl(i+1)
#
#             if nums[i] - k not in freq_map:
#                 freq_map[nums[i]] += 1
#                 total_count += impl(i+1)
#                 freq_map[nums[i]] -= 1
#                 if freq_map[nums[i]] == 0:
#                     del freq_map[nums[i]]
#             return total_count
#
#         return impl(0) - 1


# Runtime
# 71
# ms
# Beats
# 80.10%
# of users with Python3
# Memory
# 16.64
# MB
# Beats
# 53.29%
# of users with Python3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#
#         def impl(subsets, i):
#             if i == len(subsets):
#                 return 1
#
#             skip = impl(subsets, i+1)
#             take = (1 << subsets[i][1]) - 1
#
#             if i + 1 < len(subsets) and subsets[i+1][0] - subsets[i][0] == k:
#                 take *= impl(subsets, i+2)
#             else:
#                 take *= impl(subsets, i+1)
#
#             return skip + take
#
#         total_count = 1
#
#         freq_map = defaultdict(lambda: defaultdict(int))
#         for x in nums:
#             freq_map[x % k][x] += 1
#
#         for fr in freq_map.values():
#             subsets = sorted(fr.items())
#             total_count *= impl(subsets, 0)
#
#         return total_count - 1


# Runtime
# 58
# ms
# Beats
# 87.35%
# of users with Python3
# Memory
# 16.62
# MB
# Beats
# 53.29%
# of users with Python3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#
#         def impl(subsets, counts, i):
#             if i == len(subsets):
#                 return 1
#
#             if counts[i] != -1:
#                 return counts[i]
#
#             skip = impl(subsets, counts, i+1)
#             take = (1 << subsets[i][1]) - 1
#
#             if i + 1 < len(subsets) and subsets[i+1][0] - subsets[i][0] == k:
#                 take *= impl(subsets, counts, i+2)
#             else:
#                 take *= impl(subsets, counts, i+1)
#
#             counts[i] = skip + take
#             return counts[i]
#
#         total_count = 1
#
#         freq_map = defaultdict(lambda: defaultdict(int))
#         for x in nums:
#             freq_map[x % k][x] += 1
#
#         for fr in freq_map.values():
#             subsets = sorted(fr.items())
#             counts = [-1] * len(subsets)
#             total_count *= impl(subsets, counts, 0)
#
#         return total_count - 1


# Runtime
# 59
# ms
# Beats
# 86.51%
# of users with Python3
# Memory
# 16.51
# MB
# Beats
# 84.32%
# of users with Python3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#         total_count = 1
#
#         freq_map = defaultdict(lambda: defaultdict(int))
#         for x in nums:
#             freq_map[x % k][x] += 1
#
#         for fr in freq_map.values():
#             subsets = sorted(fr.items())
#             n = len(fr)
#             counts = [0] * (n+1)
#             counts[n] = 1
#
#             for i in range(n-1, -1, -1):
#                 skip = counts[i+1]
#                 take = 2 ** subsets[i][1] - 1
#                 if i + 1 < n and subsets[i+1][0] - subsets[i][0] == k:
#                     take *= counts[i+2]
#                 else:
#                     take *= counts[i + 1]
#
#                 counts[i] = skip + take
#
#             total_count *= counts[0]
#
#         return total_count - 1


# Runtime
# 54
# ms
# Beats
# 90.73%
# of users with Python3
# Memory
# 16.56
# MB
# Beats
# 84.32%
# of users with Python3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/editorial/?envType=daily-question&envId=2024-05-23
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1

        freq_map = defaultdict(lambda: defaultdict(int))
        for x in nums:
            freq_map[x % k][x] += 1

        for fr in freq_map.values():

            prev_num, curr, prev1, prev2 = -k, 1, 1, 0

            for num, freq in sorted(fr.items()):
                skip = prev1
                if num - prev_num == k:
                    take = ((1 << freq) - 1) * prev2
                else:
                    take = ((1 << freq) - 1) * prev1

                curr = skip + take
                prev2, prev1 = prev1, curr
                prev_num = num

            total_count *= curr
        return total_count - 1


tests = [
    [[2,4,6], 2, 4],
    [[1], 1, 1],
    [[10,4,5,7,2,1], 3, 23],
]

run_functional_tests(Solution().beautifulSubsets, tests)
