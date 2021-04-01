"""
https://leetcode.com/problems/next-permutation/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/583/week-5-january-29th-january-31st/3623/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List


# Runtime: 44 ms, faster than 54.18% of Python3 online submissions for Next Permutation.
# Memory Usage: 14.3 MB, less than 23.40% of Python3 online submissions for Next Permutation.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        invIdx = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                invIdx = i - 1
                break
        if invIdx == -1:
            nums.sort()
            return
        for i in range(n-1, invIdx, -1):
            if nums[i] > nums[invIdx]:
                nums[i], nums[invIdx] = nums[invIdx], nums[i]
                # tail = nums[invIdx+1:]
                # tail.reverse()
                # nums[invIdx + 1:].reverse()
                nums[invIdx + 1:] = nums[-1:invIdx:-1]
                # nums = nums[:invIdx+1] + tail
                return



tests = [
    ([1,3,2], [2,1,3]),

    ([1,2,3], [1,3,2]),
    ([3,2,1], [1,2,3]),
    ([1,1,5], [1,5,1]),
    ([1], [1])
]

for test in tests:
    result = test[0]
    Solution().nextPermutation(result)
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))