"""
https://leetcode.com/problems/two-city-scheduling/

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.



Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086


Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 54 ms, faster than 61.71% of Python3 online submissions for Two City Scheduling.
# Memory Usage: 14 MB, less than 17.48% of Python3 online submissions for Two City Scheduling.
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        nn = len(costs)
        n = nn // 2
        costs.sort(key=lambda v: v[0] - v[1])
        return reduce(lambda res, v: res + v[1], costs, 0) + reduce(lambda res, v: res + v[0]-v[1], costs[:n], 0)


tests = [
    [[[10,20],[30,200],[400,50],[30,20]], 110],
    [[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859],
    [[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], 3086]
]

run_functional_tests(Solution().twoCitySchedCost, tests)
