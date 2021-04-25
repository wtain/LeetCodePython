"""
https://leetcode.com/problems/random-pick-index/

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import random
from typing import List


# Runtime: 260 ms, faster than 99.93% of Python3 online submissions for Random Pick Index.
# Memory Usage: 18.2 MB, less than 73.66% of Python3 online submissions for Random Pick Index.
# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def pick(self, target: int) -> int:
#         result = 0
#         cnt = 1
#         for i, v in enumerate(self.nums):
#             if v == target:
#                 if random.random() < 1 / cnt:
#                     result = i
#                 cnt += 1
#
#         return result


# Runtime: 288 ms, faster than 80.86% of Python3 online submissions for Random Pick Index.
# Memory Usage: 18.3 MB, less than 73.66% of Python3 online submissions for Random Pick Index.
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = 0
        cnt = 1
        for i, v in enumerate(self.nums):
            if v == target:
                if random.randint(1, cnt) == 1:
                    result = i
                cnt += 1

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


n_samples = 10
s = Solution([1,2,3,3,3])
for i in range(n_samples):
    j = s.pick(3)
    print(j)