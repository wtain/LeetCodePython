"""
https://leetcode.com/problems/path-crossing/

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.



Example 1:


Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.


Constraints:

1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 5.75% of Python3 online submissions for Path Crossing.
# Memory Usage: 14.2 MB, less than 93.66% of Python3 online submissions for Path Crossing.
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x, y = 0, 0
        visited.add((x, y))
        for p in path:
            if p == 'N':
                y -= 1
            elif p == 'S':
                y += 1
            elif p == 'E':
                x += 1
            elif p == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


tests = [
    ["NESWW", True]
]

run_functional_tests(Solution().isPathCrossing, tests)