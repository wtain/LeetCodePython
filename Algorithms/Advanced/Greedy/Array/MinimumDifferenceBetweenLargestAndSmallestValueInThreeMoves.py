"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/?envType=daily-question&envId=2024-07-03

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.



Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.
Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.
Example 3:

Input: nums = [3,100,20]
Output: 0
Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
import heapq
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 276
# ms
# Beats
# 64.62%
# Analyze Complexity
# Memory
# 27.97
# MB
# Beats
# 12.26%
# class Solution:
#     def minDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 3:
#             return 0
#         nums.sort()
#         result = nums[-1] - nums[0]
#         m = n - 3
#         for j in range(3+1):
#             diff = nums[m+j-1] - nums[j]
#             result = min(result, diff)
#         return result


# Runtime
# 255
# ms
# Beats
# 93.16%
# Analyze Complexity
# Memory
# 28.03
# MB
# Beats
# 12.26%
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/editorial/?envType=daily-question&envId=2024-07-03
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        smallest4 = sorted(heapq.nsmallest(4, nums))
        largest4 = sorted(heapq.nlargest(4, nums))
        min_diff = math.inf
        for i in range(4):
            min_diff = min(min_diff, largest4[i] - smallest4[i])

        return min_diff


tests = [
    [[6,6,0,1,1,4,6], 2], #  0 1 1 4 6 6 6
    [[5,3,2,4], 0],
    [[1,5,0,10,14], 1], #  0 1 5 10 14
    [[3,100,20], 0],
]

run_functional_tests(Solution().minDifference, tests)
