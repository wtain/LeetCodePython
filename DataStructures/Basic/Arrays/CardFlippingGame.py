"""
https://leetcode.com/problems/card-flipping-game/

You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

After flipping the cards, an integer is considered good if it is facing down on some card and not facing up on any card.

Return the minimum possible good integer after flipping the cards. If there are no good integers, return 0.



Example 1:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation:
If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
2 is the minimum good integer as it appears facing down but not facing up.
It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.
Example 2:

Input: fronts = [1], backs = [1]
Output: 0
Explanation:
There are no good integers no matter how we flip the cards, so we return 0.


Constraints:

n == fronts.length == backs.length
1 <= n <= 1000
1 <= fronts[i], backs[i] <= 2000
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def flipgame(self, fronts: List[int], backs: List[int]) -> int:
#         n = len(fronts)
#         for i in range(n):
#             if fronts[i] > backs[i]:
#                 fronts[i], backs[i] = backs[i], fronts[i]
#         values = [value for value in fronts if value not in set(backs)]
#         return min(values) if values else 0


# Runtime
# 109 ms
# Beats
# 84.7%
# Memory
# 14.3 MB
# Beats
# 26.55%
# https://leetcode.com/problems/card-flipping-game/solutions/2479800/c-simple-c-code/
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        INT_MAX = 1 << 32
        result = INT_MAX
        hash = defaultdict(int)
        for i in range(n):
            if fronts[i] == backs[i]:
                hash[fronts[i]] += 1
        for i in range(n):
            if fronts[i] not in hash:
                result = min(result, fronts[i])
                hash[fronts[i]] += 1
            if backs[i] not in hash:
                result = min(result, backs[i])
                hash[backs[i]] += 1
        return result if result < INT_MAX else 0



tests = [
    [[1,1], [1,2], 2],
    [[1,2,4,4,7], [1,3,4,1,3], 2],
    [[1], [1], 0],
]

run_functional_tests(Solution().flipgame, tests)
