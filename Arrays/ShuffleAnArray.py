"""
https://leetcode.com/problems/shuffle-an-array/

Given an integer array nums, design an algorithm to randomly shuffle the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]



Constraints:

1 <= nums.length <= 200
-106 <= nums[i] <= 106
All the elements of nums are unique.
At most 5 * 104 calls will be made to reset and shuffle.
"""
import random
from typing import List


# Runtime: 480 ms, faster than 5.29% of Python3 online submissions for Shuffle an Array.
# Memory Usage: 19.8 MB, less than 7.08% of Python3 online submissions for Shuffle an Array.
# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def reset(self) -> List[int]:
#         return self.nums
#
#     def shuffle(self) -> List[int]:
#         n = len(self.nums)
#         mapping = [-1] * n
#         for i in range(n):
#             j = random.randint(0, n-1)
#             while mapping[j] != -1:
#                 j = random.randint(0, n - 1)
#             mapping[j] = i
#         result = [0] * n
#         for i in range(n):
#             result[mapping[i]] = self.nums[i]
#         return result


# Runtime: 328 ms, faster than 43.22% of Python3 online submissions for Shuffle an Array.
# Memory Usage: 19.4 MB, less than 39.51% of Python3 online submissions for Shuffle an Array.
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        result = self.nums.copy()
        for i in range(n):
            j = random.randint(i, n-1)
            result[i], result[j] = result[j], result[i]
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

s = Solution([1, 2, 3, 4, 5])
print(s.shuffle())
print(s.shuffle())
print(s.reset())