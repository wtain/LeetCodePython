"""
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List

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
# 32 ms
# Beats
# 84.58%
# Memory
# 13.8 MB
# Beats
# 57.18%
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            result.append(node.val)
        return result


tests = [
    [build_tree_from_list([1,null,2,3]), [1,2,3]],
    [build_tree_from_list([]), []],
    [build_tree_from_list([1]), [1]],
]

run_functional_tests(Solution().preorderTraversal, tests)
