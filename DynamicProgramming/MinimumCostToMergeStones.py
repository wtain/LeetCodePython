"""
https://leetcode.com/problems/minimum-cost-to-merge-stones/
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""
from typing import List


# Runtime: 60 ms, faster than 48.31% of Python3 online submissions for Minimum Cost to Merge Stones.
# Memory Usage: 14.7 MB, less than 59.55% of Python3 online submissions for Minimum Cost to Merge Stones.
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        if (n-1) % (K-1):
            return -1
        dp = [[-1] * n for i in range(n)]
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        def merge(l: int, r: int, k: int) -> int:
            nonlocal dp, prefix, stones
            if r - l + 1 < k:
                return 0
            if r - l + 1 == k:
                return prefix[r+1] - prefix[l]
            if dp[l][r] != -1:
                return dp[l][r]
            res = 1 << 31
            for i in range(l, r, k-1):
                res = min(res, merge(l, i, k) + merge(i+1, r, k))
            if (r - l) % (k-1) == 0:
                res += prefix[r+1] - prefix[l]
            dp[l][r] = res
            return res

        return merge(0, n-1, K)


tests = [
    ([3,2,4,1], 2, 20),
    ([3,2,4,1], 3, -1),
    ([3,5,1,2,6], 3, 25)
]

for test in tests:
    result = Solution().mergeStones(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))