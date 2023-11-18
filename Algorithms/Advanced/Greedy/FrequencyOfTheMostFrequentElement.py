"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/?envType=daily-question&envId=2023-11-18

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.



Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1156
# ms
# Beats
# 62.37%
# of users with Python3
# Memory
# 31.16
# MB
# Beats
# 55.16%
# of users with Python3
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/editorial/?envType=daily-question&envId=2023-11-18
# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         left, result, curr = 0, 0, 0
#
#         for right in range(len(nums)):
#             target = nums[right]
#             curr += target
#
#             while (right - left + 1) * target - curr > k:
#                 curr -= nums[left]
#                 left += 1
#             result = max(result, right - left + 1)
#         return result


# Runtime
# 997
# ms
# Beats
# 97.62%
# of users with Python3
# Memory
# 31.32
# MB
# Beats
# 18.27%
# of users with Python3
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/editorial/?envType=daily-question&envId=2023-11-18
# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         left, curr = 0, 0
#
#         for right in range(len(nums)):
#             target = nums[right]
#             curr += target
#
#             if (right - left + 1) * target - curr > k:
#                 curr -= nums[left]
#                 left += 1
#         return len(nums) - left


# Runtime
# 3900
# ms
# Beats
# 5.03%
# of users with Python3
# Memory
# 30.42
# MB
# Beats
# 94.09%
# of users with Python3
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/editorial/?envType=daily-question&envId=2023-11-18
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        def check(i):
            target = nums[i]
            left, right, best = 0, i, i

            while left <= right:
                mid = (left + right) // 2
                count = i - mid + 1
                final_sum = count * target
                original_sum = prefix[i] - prefix[mid] + nums[mid]
                operations_required = final_sum - original_sum

                if operations_required > k:
                    left = mid + 1
                else:
                    best = mid
                    right = mid - 1
            return i - best + 1

        nums.sort()
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        result = 0
        for i in range(len(nums)):
            result = max(result, check(i))

        return result


tests = [
    [[1,2,4], 5, 3],
    [[1,4,8,13], 5, 2],
    [[3,9,6], 2, 1],
    [[9930,9923,9983,9997,9934,9952,9945,9914,9985,9982,9970,9932,9985,9902,9975,9990,9922,9990,9994,9937,9996,9964,9943,9963,9911,9925,9935,9945,9933,9916,9930,9938,10000,9916,9911,9959,9957,9907,9913,9916,9993,9930,9975,9924,9988,9923,9910,9925,9977,9981,9927,9930,9927,9925,9923,9904,9928,9928,9986,9903,9985,9954,9938,9911,9952,9974,9926,9920,9972,9983,9973,9917,9995,9973,9977,9947,9936,9975,9954,9932,9964,9972,9935,9946,9966], 3056, 73],
]

run_functional_tests(Solution().maxFrequency, tests)
