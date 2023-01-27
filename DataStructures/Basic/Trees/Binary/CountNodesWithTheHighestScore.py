"""
https://leetcode.com/problems/count-nodes-with-the-highest-score/

There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

Return the number of nodes that have the highest score.



Example 1:

example-1
Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
Example 2:

example-2
Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.


Constraints:

n == parents.length
2 <= n <= 105
parents[0] == -1
0 <= parents[i] <= n - 1 for i != 0
parents represents a valid binary tree.
"""
from collections import defaultdict
from itertools import product, accumulate
from math import prod
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1440 ms
# Beats
# 71.8%
# Memory
# 117.7 MB
# Beats
# 56.50%
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:

        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        scores = [0] * n
        max_score, max_score_count = 0, 0

        def dfs(node: int) -> int:
            nonlocal parents, children, scores, max_score, max_score_count, n
            counts = []
            for child in children[node]:
                counts.append(dfs(child))

            children_count = sum(counts)
            nodes_above = max(n - 1 - children_count, 1)

            scores[node] = nodes_above * prod(counts)
            if scores[node] > max_score:
                max_score_count = 1
                max_score = scores[node]
            elif scores[node] == max_score:
                max_score_count += 1

            return children_count + 1

        dfs(0)

        return max_score_count


tests = [
    [[-1,2,0,2,0], 3],
    [[-1,2,0], 2],
]

run_functional_tests(Solution().countHighestScoreNodes, tests)
