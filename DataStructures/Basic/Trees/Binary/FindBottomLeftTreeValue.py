"""
https://leetcode.com/problems/find-bottom-left-tree-value/description/?envType=daily-question&envId=2024-02-28

Given the root of a binary tree, return the leftmost value in the last row of the tree.



Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from typing import Optional

from Common.Constants import null
from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests
from Common.TreeUtils import build_tree_from_list


# WRONG
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
#         left_most_val = root.val
#         level = 0
#         pos = 0
#
#         def impl(node, cur_level, cur_pos):
#             nonlocal left_most_val, level, pos
#             if cur_level > level or cur_level == level and pos > cur_pos:
#                 level = cur_level
#                 left_most_val = node.val
#                 pos = cur_pos
#             if node.left:
#                 impl(node.left, cur_level + 1, cur_pos - 1)
#             if node.right:
#                 impl(node.right, cur_level + 1, cur_pos + 1)
#
#         impl(root, 0, 0)
#
#         return left_most_val


# Runtime
# 39
# ms
# Beats
# 75.63%
# of users with Python3
# Memory
# 18.22
# MB
# Beats
# 79.63%
# of users with Python3
# https://leetcode.com/problems/find-bottom-left-tree-value/solutions/?envType=daily-question&envId=2024-02-28
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left_most_val = root.val
        level = 0

        def impl(node, cur_level):
            nonlocal left_most_val, level
            if cur_level > level:
                level = cur_level
                left_most_val = node.val
            if node.left:
                impl(node.left, cur_level + 1)
            if node.right:
                impl(node.right, cur_level + 1)

        impl(root, 0)

        return left_most_val


tests = [
    [build_tree_from_list([2,1,3]), 1],
    [build_tree_from_list([1,2,3,4,null,5,6,null,null,7]), 7],
    [build_tree_from_list([ 50, 25, 75, 2, null, 55, null, null, 5, null, 59, 4, 6, 58, null, null, null, null, 7, 57, null ]), 7],
]

run_functional_tests(Solution().findBottomLeftValue, tests)
