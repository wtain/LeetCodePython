"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/?envType=daily-question&envId=2024-08-04

You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.



Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.
Example 2:

Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
Example 3:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50


Constraints:

n == nums.length
1 <= nums.length <= 1000
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 233
# ms
# Beats
# 50.00%
# Analyze Complexity
# Memory
# 38.08
# MB
# Beats
# 67.70%
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/editorial/?envType=daily-question&envId=2024-08-04
# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         store_subarray = []
#         n = len(nums)
#         for i in range(n):
#             sum = 0
#             for j in range(i, n):
#                 sum += nums[j]
#                 store_subarray.append(sum)
#
#         store_subarray.sort()
#         range_sum = 0
#         MOD = 10 ** 9 + 7
#         for i in range(left-1, right):
#             range_sum += store_subarray[i]
#             range_sum %= MOD
#         return range_sum

# Runtime
# 276
# ms
# Beats
# 28.76%
# Analyze Complexity
# Memory
# 16.95
# MB
# Beats
# 84.07%
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/editorial/?envType=daily-question&envId=2024-08-04
# class Solution:
#     def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
#         pq = []
#         for i in range(n):
#             heapq.heappush(pq, (nums[i], i))
#
#         result = 0
#         MOD = 10**9+7
#         for i in range(1, right + 1):
#             p = heapq.heappop(pq)
#             if i >= left:
#                 result += p[0]
#                 result %= MOD
#             if p[1] < n-1:
#                 p = (p[0] + nums[p[1] + 1], p[1] + 1)
#                 heapq.heappush(pq, p)
#         return result

# Runtime
# 68
# ms
# Beats
# 96.90%
# Analyze Complexity
# Memory
# 16.79
# MB
# Beats
# 93.81%
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/editorial/?envType=daily-question&envId=2024-08-04
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10 ** 9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                current_sum += nums[j]
                window_sum += nums[j] * (j-i+1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= nums[i]
                    i += 1
                count += j-i+1
                total_sum += window_sum
            return count, total_sum

        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            max_sum = sum(nums)
            left, right = min_sum, max_sum
            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid -1
                else:
                    left = mid + 1

            count, total_sum = count_and_sum(nums, n, left)
            return total_sum - left * (count - k)

        result = (sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left-1)) % MOD

        return (result + MOD) % MOD


tests = [
    [[1,2,3,4], 4, 1, 5, 13],
    [[1,2,3,4], 4, 3, 4, 6],
    [[1,2,3,4], 4, 1, 10, 50],
]

run_functional_tests(Solution().rangeSum, tests)
