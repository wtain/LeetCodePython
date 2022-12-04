"""
https://leetcode.com/problems/minimum-average-difference/description/

You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.


Example 1:

Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.
Example 2:

Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3362 ms
# Beats
# 7.42%
# Memory
# 28.3 MB
# Beats
# 10.92%
# class Solution:
#     def minimumAverageDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         lavg, ravg = [0] * n, [0] * n
#
#         s = 0
#         for i in range(n):
#             s += nums[i]
#             lavg[i] = s // (i+1)
#
#         s = 0
#         for i in range(n):
#             s += nums[n-1-i]
#             ravg[n-1-i] = s // (i+1)
#
#         mindiff = 1 << 32
#         mini = -1
#         for i in range(n):
#             l = lavg[i]
#             r = ravg[i+1] if i < n-1 else 0
#             diff = abs(l-r)
#             if diff < mindiff:
#                 mindiff = diff
#                 mini = i
#
#         return mini


# Runtime
# 3216 ms
# Beats
# 10.34%
# Memory
# 25.3 MB
# Beats
# 45.42%
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * n
        s = 0
        for i in range(n):
            s += nums[i]
            sums[i] = s

        total = sums[-1]

        mindiff = 1 << 32
        mini = -1
        for i in range(n):
            l = sums[i] // (i+1)
            r = (total - sums[i]) // (n-i-1) if i < n-1 else 0
            diff = abs(l-r)
            if diff < mindiff:
                mindiff = diff
                mini = i

        return mini


tests = [
    [[1,1,1,1,1], 0],

    [[2,5,3,9,5,3], 3],
    [[0], 0]
]

run_functional_tests(Solution().minimumAverageDifference, tests)
