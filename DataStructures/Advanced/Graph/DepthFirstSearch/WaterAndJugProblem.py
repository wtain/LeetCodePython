"""
https://leetcode.com/problems/water-and-jug-problem/

You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.


Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example
Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true


Constraints:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 106
"""
from math import gcd

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2560 ms, faster than 29.71% of Python3 online submissions for Water and Jug Problem.
# Memory Usage: 81.9 MB, less than 16.64% of Python3 online submissions for Water and Jug Problem.
# class Solution:
#     def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
#         to_visit = [(0,0)]
#         added = set()
#         added.add((0,0))
#         while to_visit:
#             c1, c2 = to_visit.pop()
#             # Vprint(c1,c2)
#             if c1 == targetCapacity or c2 == targetCapacity or c1+c2 == targetCapacity:
#                 return True
#             neighbors = set()
#
#             if c1 < jug1Capacity:
#                 neighbors.add((jug1Capacity, c2))
#                 c1free = jug1Capacity - c1
#                 diff = min(c1free, c2)
#                 if diff > 0:
#                     neighbors.add((c1 + diff, c2 - diff))
#             if c1 > 0:
#                 neighbors.add((0, c2))
#             if c2 < jug2Capacity:
#                 neighbors.add((c1, jug2Capacity))
#                 c2free = jug2Capacity - c2
#                 diff = min(c2free, c1)
#                 if diff > 0:
#                     neighbors.add((c1 - diff, c2 + diff))
#             if c2 > 0:
#                 neighbors.add((c1, 0))
#             for neighbor in neighbors:
#                 if neighbor not in added:
#                     to_visit.append(neighbor)
#                     added.add(neighbor)
#         return False

# def gcd(a: int, b: int) -> int:
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#     return a
#

# Runtime: 28 ms, faster than 88.96% of Python3 online submissions for Water and Jug Problem.
# Memory Usage: 14.2 MB, less than 85.57% of Python3 online submissions for Water and Jug Problem.
# https://leetcode.com/problems/water-and-jug-problem/discuss/804576/Python3-1-line
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return not targetCapacity or (targetCapacity <= jug1Capacity + jug2Capacity and targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0)


tests = [
    [3, 5, 4, True],
    [2, 6, 5, False],
    [1, 2, 3, True]
]

run_functional_tests(Solution().canMeasureWater, tests)