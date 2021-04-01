"""
https://leetcode.com/problems/number-of-equivalent-domino-pairs/
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].



Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""
from typing import List


# Runtime: 360 ms, faster than 7.92% of Python3 online submissions for Number of Equivalent Domino Pairs.
# Memory Usage: 23.9 MB, less than 47.64% of Python3 online submissions for Number of Equivalent Domino Pairs.
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = 0
        seen = {}
        for (a, b) in dominoes:
            id = 10*min(a, b) + max(a,b)
            if id in seen.keys():
                cnt += seen[id]
            seen[id] = seen.get(id, 0) + 1
        return cnt


tests = [
    ([[1,2],[1,2],[1,1],[1,2],[2,2]], 3),

    ([[1,2],[2,1],[3,4],[5,6]], 1)
]

for test in tests:
    result = Solution().numEquivDominoPairs(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
