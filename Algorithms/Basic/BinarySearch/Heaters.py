"""
https://leetcode.com/problems/heaters/
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.


Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""
from bisect import bisect_left
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 484 ms, faster than 25.85% of Python3 online submissions for Heaters.
Memory Usage: 17.1 MB, less than 37.22% of Python3 online submissions for Heaters.
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        maxd = 0
        for h in houses:
            d = abs(heaters[0] - h)
            d = min(d, abs(heaters[-1] - h))
            l = bisect_left(heaters, h, 0, len(heaters))
            r = bisect_left(heaters, h+1, 0, len(heaters))
            if l < len(heaters):
                d = min(d, abs(heaters[l] - h))
                l += 1
                if l < len(heaters):
                    d = min(d, abs(heaters[l] - h))
            if r < len(heaters):
                d = min(d, abs(heaters[r] - h))
                r -= 1
                if r < len(heaters):
                    d = min(d, abs(heaters[r] - h))
            maxd = max(maxd, d)
        return maxd


tests = [
    [[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612], 161834419],
    [[1,2,3],[1,2,3], 0],
    [[1,2,3],[2], 1],
    [[1,2,3,4],[1,4], 1]
]

run_functional_tests(Solution().findRadius, tests)
