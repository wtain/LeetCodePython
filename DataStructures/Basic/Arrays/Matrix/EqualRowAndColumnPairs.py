"""
https://leetcode.com/problems/equal-row-and-column-pairs/

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).



Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""
from collections import defaultdict
from typing import List, Tuple

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2518 ms
# Beats
# 11.34%
# Memory
# 19.1 MB
# Beats
# 26.68%
# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         rowhashes, columnhashes = [0] * n, [0] * n
#         for i in range(n):
#             for j in range(n):
#                 rowhashes[i] = rowhashes[i] * 1000039 + grid[i][j]
#                 columnhashes[j] = columnhashes[j] * 1000039 + grid[i][j]
#         hash_dict = defaultdict(list)
#         equal_count = 0
#         for i in range(n):
#             hash_dict[rowhashes[i]].append(i)
#         for column in range(n):
#             for row in hash_dict[columnhashes[column]]:
#                 mismatch = False
#                 for i in range(n):
#                     if grid[i][column] != grid[row][i]:
#                         mismatch = True
#                         break
#                 if not mismatch:
#                     equal_count += 1
#         return equal_count


# Runtime
# 2639 ms
# Beats
# 10.59%
# Memory
# 37.2 MB
# Beats
# 5.7%
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        Trie = lambda: [defaultdict(Trie), []]
        trie = Trie()

        n = len(grid)
        for i in range(n):
            cur = trie
            for j in range(n):
                cur = cur[0][grid[i][j]]
            cur[1].append(i)

        equal_count = 0

        for i in range(n):
            cur = trie
            for j in range(n):
                cur = cur[0][grid[j][i]]
            for row in cur[1]:
                match = True
                for j in range(n):
                    if grid[row][j] != grid[j][i]:
                        match = False
                        break
                if match:
                    equal_count += 1

        return equal_count


tests = [
    [[[3,2,1],[1,7,6],[2,7,7]], 1],
    [[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3]
]

run_functional_tests(Solution().equalPairs, tests)
