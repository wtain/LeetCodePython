"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/?envType=daily-question&envId=2024-06-19

You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.



Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.


Constraints:

bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n

"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1159
# ms
# Beats
# 5.88%
# Analyze Complexity
# Memory
# 30.40
# MB
# Beats
# 75.28%
# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         l, r = 1, max(bloomDay)+1
#
#         def can_do(d):
#             c = 0
#             n = len(bloomDay)
#             i = 0
#             while i < n:
#                 j = 0
#                 while i < n and bloomDay[i] <= d and j < k:
#                     i += 1
#                     j += 1
#                 if j == k:
#                     c += 1
#                 else:
#                     i += 1
#             return c >= m
#
#         result = -1
#         while l < r:
#             mid = l + (r - l) // 2
#             if can_do(mid):
#                 r = mid
#                 result = mid
#             else:
#                 l = mid+1
#         return result


# Runtime
# 934
# ms
# Beats
# 25.77%
# Analyze Complexity
# Memory
# 29.55
# MB
# Beats
# 98.81%
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, r = 1, max(bloomDay)+1

        def can_do(d):
            c = 0
            bouquets = 0
            for b in bloomDay:
                if b <= d:
                    c += 1
                else:
                    c = 0
                if c == k:
                    c = 0
                    bouquets += 1
            return bouquets >= m

        result = -1
        while l < r:
            mid = l + (r - l) // 2
            if can_do(mid):
                r = mid
                result = mid
            else:
                l = mid+1
        return result


tests = [
    [[1,10,2,9,3,8,4,7,5,6], 4, 2, 9],
    [[1,10,3,10,2], 3, 1, 3],
    [[1,10,3,10,2], 3, 2, -1],
    [[7,7,7,7,12,7,7], 2, 3, 12],
]

run_functional_tests(Solution().minDays, tests)
