"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/
https://leetcode.com/problems/set-mismatch/

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.



Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
from typing import List


# Runtime: 212 ms, faster than 44.78% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.2 MB, less than 98.51% of Python3 online submissions for Set Mismatch.
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         missing = dup = -1
#         for i in range(n):
#             index = abs(nums[i])-1
#             if nums[index] > 0:
#                 nums[index] = -nums[index]
#             else:
#                 dup = abs(nums[i])
#         for i in range(n):
#             if nums[i] > 0:
#                 missing = i + 1
#                 break
#         return [dup, missing]

# Runtime: 216 ms, faster than 39.98% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.3 MB, less than 93.96% of Python3 online submissions for Set Mismatch.
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        xor = xor0 = xor1 = 0
        for x in nums:
            xor ^= x
        for i in range(1, n+1):
            xor ^= i
        rightbit = xor & ~(xor - 1)
        for x in nums:
            if rightbit & x:
                xor1 ^= x
            else:
                xor0 ^= x
        for i in range(1, n+1):
            if rightbit & i:
                xor1 ^= i
            else:
                xor0 ^= i
        return [xor0, xor1] if xor0 in nums else [xor1, xor0]


tests = [
    ([1,2,2,4], [2,3]),
    ([1,1], [1,2])
]

for test in tests:
    result = Solution().findErrorNums(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))