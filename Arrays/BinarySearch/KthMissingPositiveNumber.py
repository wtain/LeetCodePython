"""
https://leetcode.com/problems/kth-missing-positive-number/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3594/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.



Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

Runtime: 56 ms, faster than 37.93% of Python3 online submissions for Kth Missing Positive Number.
Memory Usage: 14.5 MB, less than 35.70% of Python3 online submissions for Kth Missing Positive Number.

Runtime: 52 ms, faster than 64.07% of Python3 online submissions for Kth Missing Positive Number.
Memory Usage: 14.4 MB, less than 63.22% of Python3 online submissions for Kth Missing Positive Number.
"""
from typing import List

# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         m = 0
#         c = 1
#         for ai in arr:
#             while c < ai:
#                 c += 1
#                 m += 1
#                 if m == k:
#                     return c
#         return -1

# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         h = set()
#         for ai in arr:
#             h.add(ai)
#         m = 0
#         number = 0
#         while m < k:
#             number += 1
#             while number in h:
#                 number += 1
#             m += 1
#         return number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start, end = 0, len(arr)
        while start < end:
            mid = (start + end) // 2
            if arr[mid] - mid - 1 < k:
                start = mid + 1
            else:
                end = mid
        return end + k


tests = [
    ([2,3,4,7,11], 5, 9),
    ([1,2,3,4], 2, 6)
]

for test in tests:
    result = Solution().findKthPositive(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))