"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
from typing import List


"""
Runtime: 264 ms, faster than 91.41% of Python3 online submissions for Minimum Moves to Equal Array Elements.
Memory Usage: 15.1 MB, less than 47.83% of Python3 online submissions for Minimum Moves to Equal Array Elements.
"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        vmin = min(nums)
        s = sum(nums)
        # s + k * (n-1) = A * n
        # vmin + k = A
        # s + k * (n-1) = (vmin + k) * n
        # s + k * (n-1) = vmin * n + k * n
        # s = vmin * n + k
        # k = s - vmin * n
        return s - vmin * n


print(Solution().minMoves([1,2,3]))  # 3
