"""
https://leetcode.com/problems/maximum-points-in-an-archery-competition/

Alice and Bob are opponents in an archery competition. The competition has set the following rules:

Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
The points are then calculated as follows:
The target has integer scoring sections ranging from 0 to 11 inclusive.
For each section of the target with score k (in between 0 to 11), say Alice and Bob have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice takes k points. If ak < bk, then Bob takes k points.
However, if ak == bk == 0, then nobody takes k points.
For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.

You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.

Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.

If there are multiple ways for Bob to earn the maximum total points, return any one of them.



Example 1:


Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
Output: [0,0,0,0,1,1,0,0,1,2,3,1]
Explanation: The table above shows how the competition is scored.
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.
Example 2:


Input: numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
Output: [0,0,0,0,0,0,0,0,1,1,1,0]
Explanation: The table above shows how the competition is scored.
Bob earns a total point of 8 + 9 + 10 = 27.
It can be shown that Bob cannot obtain a score higher than 27 points.


Constraints:

1 <= numArrows <= 105
aliceArrows.length == bobArrows.length == 12
0 <= aliceArrows[i], bobArrows[i] <= numArrows
sum(aliceArrows[i]) == numArrows
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 367 ms
# Beats
# 48.23%
# Memory
# 14 MB
# Beats
# 54.12%
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:

        def impl(i0, arrows):
            if i0 == -1:
                return 0, 0
            mask1 = 0
            shot = -1
            if arrows - aliceArrows[i0] - 1 >= 0:
                mask1, shot = impl(i0-1, arrows - aliceArrows[i0] - 1)
                shot += i0
                mask1 |= (1 << i0)
            mask0, no_shot = impl(i0-1, arrows)
            mask = mask1 if shot > no_shot else mask0

            return mask, max(shot, no_shot)

        mask, score = impl(11, numArrows)
        result = [0] * 12
        for i in range(12):
            if mask & (1 << i):
                result[i] = aliceArrows[i] + 1

        result[0] = numArrows - sum(result[1:])

        return result


tests = [
    [9, [1,1,0,1,0,0,2,1,0,1,2,0], [0,0,0,0,1,1,0,0,1,2,3,1]],
    [3, [0,0,1,0,0,0,0,0,0,0,0,2], [0,0,0,0,0,0,0,0,1,1,1,0]],
    [89, [3,2,28,1,7,1,16,7,3,13,3,5], [21,3,0,2,8,2,17,8,4,14,4,6]],
]

run_functional_tests(Solution().maximumBobPoints, tests)
