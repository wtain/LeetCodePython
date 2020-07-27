"""
https://leetcode.com/problems/arranging-coins/
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""
from math import sqrt, floor

"""
Runtime: 32 ms, faster than 88.58% of Python3 online submissions for Arranging Coins.
Memory Usage: 14 MB, less than 22.70% of Python3 online submissions for Arranging Coins.]
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # n >= sum(1..k) = (1 + k)*k/2
        # 2*n >= k*(k+1)
        # k = sqrt(2*n)
        return int((2 * sqrt(2*n+1)-1) / 2)


print(Solution().arrangeCoins(0))  # 0
print(Solution().arrangeCoins(5))  # 2
print(Solution().arrangeCoins(8))  # 3
print(Solution().arrangeCoins(1804289383))  # 60070

