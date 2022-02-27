"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.



Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).


Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#
#         max_width = 0
#
#         def impl(node_left: TreeNode, node_right: TreeNode, l: int, r: int):
#             nonlocal max_width
#             w = r - l
#             max_width = max(max_width, w)
#             if node_left:
#                 if node_left.left:
#                     node_left = node_left.left
#                     l -= 1
#                 elif node_left.right:
#                     node_left = node_left.right
#
#
#         if root:
#             impl(root, root, 0, 0)
#
#         return max_width


# Runtime: 48 ms, faster than 79.11% of Python3 online submissions for Maximum Width of Binary Tree.
# Memory Usage: 19 MB, less than 11.15% of Python3 online submissions for Maximum Width of Binary Tree.
# https://leetcode.com/submissions/detail/364257053/
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        bounds = []

        def impl(node: TreeNode, level: int, pos: int):
            nonlocal bounds
            if level >= len(bounds):
                bounds.append([pos, pos])
            else:
                bounds[level] = [min(bounds[level][0], pos), max(bounds[level][1], pos)]
            if node.left:
                impl(node.left, level+1, 2*pos)
            if node.right:
                impl(node.right, level + 1, 2 * pos + 1)

        impl(root, 0, 0)
        return max(p[1] - p[0] + 1 for p in bounds)


# WRONG
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return 1
#
#         max_width = 0
#
#         def impl(l, r):
#             nonlocal max_width
#             l_node, l_pos = l
#             r_node, r_pos = r
#             max_width = max(max_width, r_pos - l_pos + 1)
#
#             if l_node and l_node.left:
#                 l_node = l_node.left
#                 l_pos = 2 * l_pos
#             elif l_node and l_node.right:
#                 l_node = l_node.right
#                 l_pos = 2 * l_pos + 1
#             elif r_node and r_node.left:
#                 l_node = r_node.left
#                 l_pos = 2 * r_pos
#             elif r_node and r_node.right:
#                 l_node = r_node.right
#                 l_pos = 2 * r_pos + 1
#             else:
#                 l_node = None
#
#             if r_node and r_node.right:
#                 r_node = r_node.right
#                 r_pos = 2 * r_pos + 1
#             elif r_node and r_node.left:
#                 r_node = r_node.left
#                 r_pos = 2 * r_pos
#             elif l_node and l_node.right:
#                 r_node = l_node.right
#                 r_pos = 2 * l_pos + 1
#             elif l_node and l_node.left:
#                 r_node = l_node.left
#                 r_pos = 2 * l_pos
#             else:
#                 r_node = None
#
#             if l_node or r_node:
#                 impl([l_node, l_pos], [r_node, r_pos])
#
#         impl([root, 0], [root, 0])
#         return max_width


tests = [
    [build_tree_from_list([1,3,2,5,3,null,9]), 4],
    [build_tree_from_list([1,3,null,5,3]), 2],
    [build_tree_from_list([1,3,2,5]), 2],
    [build_tree_from_list([1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2]), 8]
]

run_functional_tests(Solution().widthOfBinaryTree, tests)
