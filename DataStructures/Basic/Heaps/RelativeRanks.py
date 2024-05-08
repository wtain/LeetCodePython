"""
https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.



Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].



Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
"""
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 56
# ms
# Beats
# 93.52%
# of users with Python3
# Memory
# 17.79
# MB
# Beats
# 50.24%
# of users with Python3
# class Solution:
#     def findRelativeRanks(self, score: List[int]) -> List[str]:
#         n = len(score)
#         entries = [(score[i], i) for i in range(n)]
#         entries.sort(reverse=True)
#         result = [0] * n
#         for j in range(n):
#             i = entries[j][1]
#             if j == 0:
#                 result[i] = "Gold Medal"
#             elif j == 1:
#                 result[i] = "Silver Medal"
#             elif j == 2:
#                 result[i] = "Bronze Medal"
#             else:
#                 result[i] = str(j+1)
#         return result


# Runtime
# 67
# ms
# Beats
# 51.66%
# of users with Python3
# Memory
# 17.68
# MB
# Beats
# 71.46%
# of users with Python3
# https://leetcode.com/problems/relative-ranks/editorial/?envType=daily-question&envId=2024-05-08
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        m = max(score)
        score_to_index = [0] * (m+1)
        for i in range(n):
            score_to_index[score[i]] = i+1
        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = [None] * n
        place = 1
        for i in range(m, -1, -1):
            if score_to_index[i] != 0:
                original_index = score_to_index[i] - 1
                if place < 4:
                    rank[original_index] = MEDALS[place-1]
                else:
                    rank[original_index] = str(place)
                place += 1
        return rank


tests = [
    [[5,4,3,2,1], ["Gold Medal","Silver Medal","Bronze Medal","4","5"]],
    [[10,3,8,9,4], ["Gold Medal","5","Bronze Medal","Silver Medal","4"]],
]

run_functional_tests(Solution().findRelativeRanks, tests)
