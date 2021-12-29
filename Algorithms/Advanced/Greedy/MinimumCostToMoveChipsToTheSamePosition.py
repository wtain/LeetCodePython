"""
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.



Example 1:


Input: position = [1,2,3]
Output: 1
Explanation: First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.
Example 2:


Input: position = [2,2,2,3,3]
Output: 2
Explanation: We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
Example 3:

Input: position = [1,1000000000]
Output: 1


Constraints:

1 <= position.length <= 100
1 <= position[i] <= 10^9
"""
from typing import List


# Runtime: 28 ms, faster than 90.17% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
# Memory Usage: 14.1 MB, less than 94.66% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
# Runtime: 48 ms, faster than 10.29% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
# Memory Usage: 14.2 MB, less than 80.87% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counts = [0] * 2
        for p in position:
            counts[p % 2] += 1
        return min(counts)


tests = [
    ([1,2,3], 1),
    ([2,2,2,3,3], 2),
    ([1,1000000000], 1)
]

for test in tests:
    result = Solution().minCostToMoveChips(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
