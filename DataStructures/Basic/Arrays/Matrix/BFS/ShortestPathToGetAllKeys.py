"""
https://leetcode.com/problems/shortest-path-to-get-all-keys/

You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.



Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 316 ms
# Beats
# 62.62%
# Memory
# 21 MB
# Beats
# 81.47%
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        i0, j0 = 0, 0
        allkeysmask = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    i0, j0 = i, j
                if 'a' <= grid[i][j] <= 'f':
                    allkeysmask |= 1 << (ord(grid[i][j]) - ord('a'))
        level = {(i0, j0, 0)}
        visited = {(i0, j0, 0)}
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        steps = 0
        while level:
            nextlevel = set()
            for i, j, keys in level:
                if keys == allkeysmask:
                    return steps
                visited.add((i, j, keys))
                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    keys1 = keys
                    if i1 < 0 or j1 < 0 or i1 >= n or j1 >= m:
                        continue
                    if grid[i1][j1] == '#':
                        continue
                    if 'A' <= grid[i1][j1] <= 'F':
                        mask = 1 << (ord(grid[i1][j1]) - ord('A'))
                        if keys & mask == 0:
                            continue
                    if 'a' <= grid[i1][j1] <= 'f':
                        keys1 |= 1 << (ord(grid[i1][j1]) - ord('a'))
                    if (i1, j1, keys1) in visited:
                        continue
                    nextlevel.add((i1, j1, keys1))
            level = nextlevel
            steps += 1
        return -1


tests = [
    [["@.a..","###.#","b.A.B"], 8],
    [["@..aA","..B#.","....b"], 6],
    [["@Aa"], -1],
]

run_functional_tests(Solution().shortestPathAllKeys, tests)
