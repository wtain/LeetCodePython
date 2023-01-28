"""
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.



Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.


Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.
"""
from collections import defaultdict
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Runtime
# 837 ms
# Beats
# 72.72%
# Memory
# 156.2 MB
# Beats
# 36.65%
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        neighbors = defaultdict(list)

        def dfs(node: TreeNode, parent: TreeNode):
            nonlocal neighbors
            if not node:
                return
            if parent:
                neighbors[parent.val].append(node.val)
                neighbors[node.val].append(parent.val)
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        time_to_infect = -1
        level = [start]
        visited = set()
        while level:
            next_level = []
            time_to_infect += 1
            for node in level:
                visited.add(node)
                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        next_level.append(neighbor)
            level = next_level

        return time_to_infect


tests = [
    [build_tree_from_list([1,5,3,null,4,10,6,9,2]), 3, 4],
    [build_tree_from_list([1]), 1, 0],
]

run_functional_tests(Solution().amountOfTime, tests)
