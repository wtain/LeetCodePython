"""
https://leetcode.com/problems/build-a-matrix-with-conditions/description/?envType=daily-question&envId=2024-07-21

You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.



Example 1:


Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
Example 2:

Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.


Constraints:

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 104
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
"""
from collections import defaultdict, deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 605
# ms
# Beats
# 6.87%
# Analyze Complexity
# Memory
# 25.42
# MB
# Beats
# 45.80%
# https://leetcode.com/problems/build-a-matrix-with-conditions/editorial/?envType=daily-question&envId=2024-07-21
# class Solution:
#     def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
#         order_rows = self.topoSort(rowConditions, k)
#         order_cols = self.topoSort(colConditions, k)
#
#         if not order_rows or not order_cols:
#             return []
#
#         matrix = [[0] * k for _ in range(k)]
#         pos_row = {num: i for i, num in enumerate(order_rows)}
#         pos_col = {num: i for i, num in enumerate(order_cols)}
#
#         for num in range(1, k+1):
#             if num in pos_row and num in pos_col:
#                 matrix[pos_row[num]][pos_col[num]] = num
#         return matrix
#
#     def topoSort(self, edges: List[List[int]], n: int) -> List[int]:
#         adj = defaultdict(list)
#         order = []
#         visited = [0] * (n+1)
#         has_cycle = [False]
#
#         for x, y in edges:
#             adj[x].append(y)
#
#         for i in range(1, n+1):
#             if visited[i] == 0:
#                 self.dfs(i, adj, visited, order, has_cycle)
#                 if has_cycle[0]:
#                     return []
#         order.reverse()
#         return order
#
#     def dfs(self, node: int, adj: defaultdict, visited: List[int], order: List[int], has_cycle: List[bool]):
#         visited[node] = 1
#         for neighbor in adj[node]:
#             if visited[neighbor] == 0:
#                 self.dfs(neighbor, adj, visited, order, has_cycle)
#                 if has_cycle[0]:
#                     return
#             elif visited[neighbor] == 1:
#                 has_cycle[0] = True
#                 return
#         visited[node] = 2
#         order.append(node)


# Runtime
# 564
# ms
# Beats
# 96.18%
# Analyze Complexity
# Memory
# 25.44
# MB
# Beats
# 45.80%
# https://leetcode.com/problems/build-a-matrix-with-conditions/editorial/?envType=daily-question&envId=2024-07-21
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        order_rows = self.toposort(rowConditions, k)
        order_cols = self.toposort(colConditions, k)

        if not order_rows or not order_cols:
            return []

        matrix = [[0] * k for _ in range(k)]
        pos_row = {num: i for i, num in enumerate(order_rows)}
        pos_col = {num: i for i, num in enumerate(order_cols)}

        for num in range(1, k+1):
            if num in pos_row and num in pos_col:
                matrix[pos_row[num]][pos_col[num]] = num
        return matrix

    def toposort(self, edges, n):
        adj = [[] for _ in range(n+1)]
        deg = [0] * (n+1)
        order = []
        for x in edges:
            adj[x[0]].append(x[1])
            deg[x[1]] += 1
        q = deque()
        for i in range(1, n+1):
            if deg[i] == 0:
                q.append(i)
        while q:
            f = q.popleft()
            order.append(f)
            n -= 1
            for v in adj[f]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        if n != 0:
            return []
        return order


tests = [
    [3, [[1,2],[3,2]], [[2,1],[3,2]], [[3,0,0],[0,0,1],[0,2,0]]],
    [3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]], []],
]


def customCheck(test, result):
    n = len(result)
    rows, cols = dict(), dict()
    for i in range(n):
        for j in range(n):
            rows[result[i][j]] = i
            cols[result[i][j]] = j
    rowConditions, colConditions = test[1], test[2]
    for above, below in rowConditions:
        if above not in rows or below not in rows:
            continue
        if rows[above] >= rows[below]:
            return False
    for left, right in colConditions:
        if left not in cols or right not in cols:
            continue
        if cols[left] >= cols[right]:
            return False
    return True


run_functional_tests(Solution().buildMatrix, tests, custom_check=customCheck)
