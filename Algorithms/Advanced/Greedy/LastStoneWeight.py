"""
https://leetcode.com/problems/last-stone-weight/

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
import heapq
from typing import List


# Runtime: 24 ms, faster than 95.91% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 14.3 MB, less than 53.00% of Python3 online submissions for Last Stone Weight.
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 78.86% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.9 MB, less than 68.03% of Python3 online submissions for Last Stone Weight.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -(y-x))
        return -stones[0] if len(stones) == 1 else 0


tests = [
    [[2,7,4,1,8,1], 1],
    [[1, 1], 0]
]

run_functional_tests(Solution().lastStoneWeight, tests)
