"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3606/
https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import heapq
import random
from typing import List


# Runtime: 56 ms, faster than 96.40% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.2 MB, less than 46.58% of Python3 online submissions for Kth Largest Element in an Array.
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]

# Runtime: 68 ms, faster than 52.52% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 46.58% of Python3 online submissions for Kth Largest Element in an Array.
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         h = []
#         for ai in nums:
#             heapq.heappush(h, ai)
#             if len(h) > k:
#                 heapq.heappop(h)
#         return heapq.heappop(h)

# Runtime: 100 ms, faster than 23.69% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.2 MB, less than 21.97% of Python3 online submissions for Kth Largest Element in an Array.
# class Solution:
#
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#
#         k = n - k + 1
#
#         for i in range(n-1, -1, -1):
#             j = random.randint(0, i)
#             tmp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = tmp
#
#         def getMiddle(l: int, r: int):
#             i = l
#             nonlocal nums
#             for j in range(l + 1, r + 1):
#                 if nums[j] < nums[l]:
#                     i += 1
#                     tmp = nums[j]
#                     nums[j] = nums[i]
#                     nums[i] = tmp
#             tmp = nums[l]
#             nums[l] = nums[i]
#             nums[i] = tmp
#             return i
#
#         l = 0
#         r = n-1
#         k -= 1
#         while l < r:
#             m = getMiddle(l, r)
#             if m == k:
#                 break
#             elif k < m:
#                 r = m - 1
#             else:
#                 l = m + 1
#         return nums[k]

# Runtime: 84 ms, faster than 27.32% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 15.1 MB, less than 74.25% of Python3 online submissions for Kth Largest Element in an Array.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for ai in nums:
            if len(h) < k or h[0] < ai:
                heapq.heappush(h, ai)
                if len(h) > k:
                    heapq.heappop(h)
        return heapq.heappop(h)


tests = [
    ([3,2,1,5,6,4], 2, 5),
    ([3,2,3,1,2,4,5,5,6], 4, 4)
]

for test in tests:
    result = Solution().findKthLargest(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))