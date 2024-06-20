"""
https://leetcode.com/problems/magnetic-force-between-two-balls/description/?envType=daily-question&envId=2024-06-20

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.



Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.


Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length

"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 910
# ms
# Beats
# 53.28%
# Analyze Complexity
# Memory
# 30.07
# MB
# Beats
# 87.18%
# class Solution:
#     def maxDistance(self, position: List[int], m: int) -> int:
#
#         def can_place(min_distance):
#             to_place = m-1
#             prev = position[0]
#             n = len(position)
#             for i in range(1, n):
#                 if position[i] - prev >= min_distance:
#                     prev = position[i]
#                     to_place -= 1
#                     if to_place == 0:
#                         return True
#             return False
#
#         position.sort()
#         l, r = 1, position[-1] - position[0] + 1
#         result = -1
#         while l < r:
#             mid = l + (r-l) // 2
#             if not can_place(mid):
#                 r = mid
#             else:
#                 result = max(result, mid) if result != -1 else mid
#                 l = mid+1
#
#         return result


# Runtime
# 645
# ms
# Beats
# 94.59%
# Analyze Complexity
# Memory
# 30.71
# MB
# Beats
# 7.69%
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def can_place(min_distance):
            to_place = m-1
            prev = position[0]
            n = len(position)
            for i in range(1, n):
                if position[i] - prev >= min_distance:
                    prev = position[i]
                    to_place -= 1
                    if to_place == 0:
                        return True
            return False

        position.sort()
        l, r = 1, int(position[-1] / (m-1))+1
        result = -1
        while l < r:
            mid = l + (r-l) // 2
            if not can_place(mid):
                r = mid
            else:
                result = mid
                l = mid+1

        return result


tests = [
    [[1,2,3,4,7], 3, 3],
    [[5,4,3,2,1,1000000000], 2, 999999999],
]

run_functional_tests(Solution().maxDistance, tests)
