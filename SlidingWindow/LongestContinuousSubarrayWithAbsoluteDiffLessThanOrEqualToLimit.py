"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.



Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
from typing import List, Deque


# Runtime: 2876 ms, faster than 5.02% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
# Memory Usage: 24.2 MB, less than 68.49% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
# class Solution:
#     def longestSubarray(self, nums: List[int], limit: int) -> int:
#         n = len(nums)
#
#         l = 0
#         result = 0
#         items = {}
#         for r in range(n):
#             items[nums[r]] = items.get(nums[r], 0) + 1
#             while max(items.keys()) - min(items.keys()) > limit and items:
#                 items[nums[l]] -= 1
#                 if not items[nums[l]]:
#                     items.pop(nums[l])
#                 l += 1
#             result = max(result, r - l + 1)
#
#         return result

# Runtime: 868 ms, faster than 35.32% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
# Memory Usage: 36.4 MB, less than 6.52% of Python3 online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        l = 0
        result = 0
        mx = Deque()
        mn = Deque()
        mx.append([nums[0], 0])
        mn.append([nums[0], 0])
        for r in range(n):

            while mx and nums[r] > mx[-1][0]:
                mx.pop()
            mx.append([nums[r], r])

            while mn and nums[r] < mn[-1][0]:
                mn.pop()
            mn.append([nums[r], r])

            while l <= r and mx[0][0] - mn[0][0] > limit:
                l += 1

                while mx and l > mx[0][1]:
                    mx.popleft()

                while mn and l > mn[0][1]:
                    mn.popleft()

            result = max(result, r - l + 1)

        return result


tests = [
    ([8,2,4,7], 4, 2),
    ([10,1,2,4,7,2], 5, 4),
    ([4,2,2,2,4,4,2,2], 0, 3)
]

for test in tests:
    result = Solution().longestSubarray(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))