"""
https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.



Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]


Constraints:

The number of nodes in the tree is in the range [1, 5000].
-105 <= Node.val <= 105
-109 <= limit <= 109
"""
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
# 124 ms
# Beats
# 43.65%
# Memory
# 15.5 MB
# Beats
# 52.28%
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(node: TreeNode, currentSum: int) -> (bool, int):
            nonlocal limit
            if not node:
                return False, float('-Inf')
            currentSum += node.val
            if not node.left and not node.right:
                return currentSum >= limit, currentSum
            left_retain, left_sum = dfs(node.left, currentSum)
            right_retain, right_sum = dfs(node.right, currentSum)
            if not left_retain:
                node.left = None
            if not right_retain:
                node.right = None
            max_sum = max(left_sum, right_sum)
            return max_sum >= limit, max_sum

        return root if dfs(root, 0)[0] else None


tests = [
    [build_tree_from_list([1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]), 1, build_tree_from_list([1,2,3,4,null,null,7,8,9,null,14])],
    [build_tree_from_list([5,4,8,11,null,17,4,7,1,null,null,5,3]), 22, build_tree_from_list([5,4,8,11,null,17,4,7,null,null,null,5])],
    [build_tree_from_list([1,2,-3,-5,null,4,null]), -1, build_tree_from_list([1,null,-3,4])],
]

run_functional_tests(Solution().sufficientSubset, tests)
# run_functional_tests(Solution().sufficientSubset, tests, run_tests=3)
