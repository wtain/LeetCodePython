"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.



Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""
from typing import List


## WRONG
# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         n = len(nums)
#         i1 = 0
#         i2 = n-1
#         cnt = 0
#         while i1 <= i2 and x > 0:
#             if nums[i1] > x and nums[i2] > x:
#                 return -1
#             if nums[i1] > x:
#                 x -= nums[i2]
#                 i2 -= 1
#             elif nums[i2] > x:
#                 x -= nums[i1]
#                 i1 += 1
#             else:
#                 if nums[i1] > nums[i2]:
#                     x -= nums[i1]
#                     i1 += 1
#                 else:
#                     x -= nums[i2]
#                     i2 -= 1
#             cnt += 1
#         return cnt if x == 0 else -1

# Runtime: 1172 ms, faster than 73.09% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 28.4 MB, less than 73.66% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# class Solution:
#     def minOperations(self, nums: List[int], x: int) -> int:
#         n = len(nums)
#         s = sum(nums)
#         t = s - x
#         i1 = 0
#         cs = 0
#         result = -1
#         for i2 in range(n+1):
#             if cs == t:
#                 l = i2 - i1
#                 r = n - l
#                 if r < result or result == -1:
#                     result = r
#             if i2 < n:
#                 cs += nums[i2]
#             while cs > t and i1 < i2:
#                 cs -= nums[i1]
#                 i1 += 1
#
#         return result

# Runtime: 1168 ms, faster than 74.17% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 28.7 MB, less than 62.40% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = sum(nums)
        t = s - x
        if t == 0:
            return n
        current = 0
        i1 = 0
        i2 = 0
        longest = 0
        while i1 < n and i2 < n:
            if current < t:
                current += nums[i2]
                i2 += 1
            elif current > t:
                current -= nums[i1]
                i1 += 1
            else:
                longest = max(longest, i2-i1)
                current -= nums[i1]
                i1 += 1
        if current == t:
            longest = max(longest, i2-i1)
        if longest == 0:
            return -1
        return n - longest



tests = [

    ([5,2,3,1,1], 5, 1),

    ([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365, 16),

    ([5207,5594,477,6938,8010,7606,2356,6349,3970,751,5997,6114,9903,3859,6900,7722,2378,1996,8902,228,4461,90,7321,7893,4879,9987,1146,8177,1073,7254,5088,402,4266,6443,3084,1403,5357,2565,3470,3639,9468,8932,3119,5839,8008,2712,2735,825,4236,3703,2711,530,9630,1521,2174,5027,4833,3483,445,8300,3194,8784,279,3097,1491,9864,4992,6164,2043,5364,9192,9649,9944,7230,7224,585,3722,5628,4833,8379,3967,5649,2554,5828,4331,3547,7847,5433,3394,4968,9983,3540,9224,6216,9665,8070,31,3555,4198,2626,9553,9724,4503,1951,9980,3975,6025,8928,2952,911,3674,6620,3745,6548,4985,5206,5777,1908,6029,2322,2626,2188,5639], 565610, 113),

    ([1,1], 3, -1),

    ([1,1,4,2,3], 5, 2),
    ([5,6,7,8,9], 4, -1),
    ([3,2,20,1,1,3], 10, 5)
]

for test in tests:
    result = Solution().minOperations(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
