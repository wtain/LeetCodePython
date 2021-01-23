"""
https://leetcode.com/problems/find-the-most-competitive-subsequence/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3611/
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.



Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
1 <= k <= nums.length
"""
from typing import List


# TLE
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         start = 0
#         n = len(nums)
#         for i in range(k):
#             val, idx = min((val, idx) for (idx, val) in enumerate(nums[start:n-k+i+1]))
#             idx += start
#             result.append(val)
#             start = idx + 1
#
#         return result


# TLE
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         n = len(nums)
#         for i in range(n):
#             m = len(result)
#             added = False
#             minj = max(k+i-n, 0)
#             for j in range(minj, m):
#                 if result[j] > nums[i]:
#                     result = result[:j]
#                     result.append(nums[i])
#                     added = True
#                     # k - j left to fill
#                     # n - i left to check
#                     # k - j <= n - i
#                     # j >= k+i-n
#                     break
#             if not added and m < k:
#                 result.append(nums[i])
#
#         return result


# Runtime: 2348 ms, faster than 5.01% of Python3 online submissions for Find the Most Competitive Subsequence.
# Memory Usage: 27.1 MB, less than 89.57% of Python3 online submissions for Find the Most Competitive Subsequence.
# class Solution:
#     def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         maxes = []
#         n = len(nums)
#         for i in range(n):
#             m = len(result)
#             added = False
#             minj = max(k+i-n, 0)
#             if m > 0 and maxes[-1] > nums[i]:
#                 for j in range(minj, m):
#                     # first item > nums[i]
#                     if result[j] > nums[i]:
#                         result = result[:j]
#                         maxes = maxes[:j]
#                         result.append(nums[i])
#                         if len(maxes) > 0:
#                             maxes.append(max(maxes[-1], nums[i]))
#                         else:
#                             maxes.append(nums[i])
#                         added = True
#                         # k - j left to fill
#                         # n - i left to check
#                         # k - j <= n - i
#                         # j >= k+i-n
#                         break
#             if not added and m < k:
#                 result.append(nums[i])
#                 if len(maxes) > 0:
#                     mx = max(maxes[-1], nums[i])
#                 else:
#                     mx = nums[i]
#                 maxes.append(mx)
#
#         return result

# Runtime: 1448 ms, faster than 28.06% of Python3 online submissions for Find the Most Competitive Subsequence.
# Memory Usage: 27 MB, less than 89.57% of Python3 online submissions for Find the Most Competitive Subsequence.
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            m = len(result)
            # leftToFill = k - m
            # leftToCheck = n - i
            while len(result) > 0 and result[-1] > nums[i] and k - len(result) + 1 <= n - i:
                result.pop()
            result.append(nums[i])

        return result[:k]



tests = [
    ([3,5,2,6], 2, [2,6]),
    ([2,4,3,3,5,4,9,6], 4, [2,3,3,4]),
]

for test in tests:
    result = Solution().mostCompetitive(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))