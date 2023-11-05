"""
https://leetcode.com/problems/find-the-winner-of-an-array-game/description/?envType=daily-question&envId=2023-11-05

Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.



Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.


Constraints:

2 <= arr.length <= 105
1 <= arr[i] <= 106
arr contains distinct integers.
1 <= k <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 506ms
# Beats 95.11%of users with Python3
# Memory
# Details
# 29.43MB
# Beats 94.02%of users with Python3
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        times = 0
        n = len(arr)
        for i in range(1, n):
            if winner < arr[i]:
                winner = arr[i]
                times = 1
            else:
                times += 1
            if times == k:
                return winner
        return winner


tests = [
    [[2,1,3,5,4,6,7], 2, 5],
    [[3,2,1], 10, 3],
    [[1,25,35,42,68,70], 1, 25],
]

run_functional_tests(Solution().getWinner, tests)
