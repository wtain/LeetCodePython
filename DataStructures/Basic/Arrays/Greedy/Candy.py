"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3793/
https://leetcode.com/problems/candy/

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.


Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 208 ms, faster than 21.27% of Python3 online submissions for Candy.
# Memory Usage: 18.1 MB, less than 10.98% of Python3 online submissions for Candy.
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         arr = sorted([(r, i) for i, r in enumerate(ratings)])
#         result = [1] * n
#         for i in range(1, n):
#             j = arr[i][1]
#             res = 1
#             if j > 0 and ratings[j] > ratings[j-1]:
#                 res = max(res, result[j-1] + 1)
#             if j < n-1 and ratings[j] > ratings[j+1]:
#                 res = max(res, result[j+1] + 1)
#             result[j] = res
#         # print(result)
#         return sum(result)


# WRONG
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         result = n
#         candies = [1] * n
#         for i in range(1, n):
#             if ratings[i] > ratings[i-1]:
#                 candies[i] = candies[i-1] + 1
#             result += candies[i] - 1
#         for i in range(n-2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 diff = candies[i+1]+1 - candies[i]
#                 candies[i] = candies[i+1]+1
#                 result += diff
#         print(candies)
#         return result


# https://leetcode.com/problems/candy/solution/
# Runtime: 164 ms, faster than 62.15% of Python3 online submissions for Candy.
# Memory Usage: 16.9 MB, less than 45.17% of Python3 online submissions for Candy.
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         left2right, right2left = [1] * n, [1] * n
#         for i in range(1, n):
#             if ratings[i] > ratings[i-1]:
#                 left2right[i] = left2right[i-1] + 1
#         for i in range(n-2,-1,-1):
#             if ratings[i] > ratings[i+1]:
#                 right2left[i] = right2left[i+1] + 1
#         return sum(max(l,r) for l, r in zip(left2right, right2left))


# Runtime: 164 ms, faster than 62.15% of Python3 online submissions for Candy.
# Memory Usage: 16.6 MB, less than 77.76% of Python3 online submissions for Candy.
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         candies = [1] * n
#         for i in range(1, n):
#             if ratings[i] > ratings[i-1]:
#                 candies[i] = max(candies[i-1] + 1, candies[i])
#         for i in range(n-2,-1,-1):
#             if ratings[i] > ratings[i+1]:
#                 candies[i] = max(candies[i+1] + 1, candies[i])
#         return sum(candies)


# Runtime: 152 ms, faster than 92.27% of Python3 online submissions for Candy.
# # Memory Usage: 16.9 MB, less than 45.17% of Python3 online submissions for Candy.
# class Solution:
#
#     def count(self, n: int) -> int:
#         return n * (n+1) // 2
#
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         if n <= 1:
#             return n
#         candies, up, down, old_slope = 0, 0, 0, 0
#         for i in range(1, n):
#             new_slope = 1 if ratings[i] > ratings[i-1] else (-1 if ratings[i] < ratings[i-1] else 0)
#             if old_slope > 0 and new_slope == 0 or old_slope < 0 and new_slope >= 0:
#                 candies += self.count(up) + self.count(down) + max(up, down)
#                 up, down = 0, 0
#             if new_slope > 0:
#                 up += 1
#             elif new_slope < 0:
#                 down += 1
#             else:
#                 candies += 1
#             old_slope = new_slope
#         candies += self.count(up) + self.count(down) + max(up, down) + 1
#         return candies

# https://leetcode.com/problems/candy/discuss/135698/Simple-solution-with-one-pass-using-O(1)-space
# Runtime: 148 ms, faster than 96.20% of Python3 online submissions for Candy.
# Memory Usage: 16.7 MB, less than 61.53% of Python3 online submissions for Candy.
class Solution:

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        candies, up, down, peak = 1, 0, 0, 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                up += 1
                peak = up
                down = 0
                candies += 1 + up
            elif ratings[i] == ratings[i-1]:
                peak = up = down = 0
                candies += 1
            else:
                up = 0
                down += 1
                candies += 1 + down - (1 if peak >= down else 0)
        return candies


tests = [
    [[1,3,4,5,2], 11],

    [[1,0,2], 5],
    [[1,2,2], 4]
]

run_functional_tests(Solution().candy, tests)