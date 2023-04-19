"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.



Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""
from functools import cache
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
# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         LEFT, RIGHT = 0, 1
#
#         @cache
#         def dp(node: TreeNode, direction):
#             if not node:
#                 return 0
#             if not node.left and not node.right:
#                 return 0
#             left_left, left_right = 0, 0
#             right_left, right_right = 0, 0
#             if node.left:
#                 left_left, left_right = dp(node.left, LEFT), dp(node.left, RIGHT)
#             if node.right:
#                 right_left, right_right = dp(node.right, LEFT), dp(node.right, RIGHT)
#             return max(left_left,
#                        left_right+1 if direction == LEFT else 0,
#                        right_left+1 if direction == RIGHT else 0,
#                        right_right)
#
#         return max(dp(root, LEFT), dp(root, RIGHT))

# WRONG
# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         LEFT, RIGHT = 0, 1
#
#         @cache
#         def dp(node: TreeNode, direction):
#             nonlocal LEFT, RIGHT
#             if not node:
#                 return 0
#             if not node.left and not node.right:
#                 return 1
#             left, right = 0, 0
#             if node.left:
#                 left = dp(node.left, LEFT)
#             if node.right:
#                 right = dp(node.right, RIGHT)
#             return max(left,
#                        right,
#                        left+1 if direction == RIGHT else 0,
#                        right+1 if direction == LEFT else 0)
#
#         return max(dp(root, LEFT), dp(root, RIGHT)) - 1


# WRONG
# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         LEFT, RIGHT = 0, 1
#
#         def dp(node: TreeNode, direction):
#             nonlocal LEFT, RIGHT
#             if not node:
#                 return 0
#             if not node.left and not node.right:
#                 return 0
#             left, right = 0, 0
#             if node.left:
#                 left = dp(node.left, LEFT)
#             if node.right:
#                 right = dp(node.right, RIGHT)
#             if direction == RIGHT:
#                 left += 1
#             if direction == LEFT:
#                 right += 1
#             return max(left, right)
#
#         return max(dp(root, LEFT), dp(root, RIGHT)) - 1


# Runtime
# 532 ms
# Beats
# 20.51%
# Memory
# 61.9 MB
# Beats
# 25.64%
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/editorial/
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT, RIGHT = 0, 1
        result = 0

        def dp(node: TreeNode, direction, steps):
            nonlocal result
            nonlocal LEFT, RIGHT
            if node:
                result = max(result, steps)
                if direction == LEFT:
                    dp(node.left, RIGHT, steps+1)
                    dp(node.right, LEFT, 1)
                else:
                    dp(node.left, RIGHT, 1)
                    dp(node.right, LEFT, steps+1)

        dp(root, LEFT, 0)
        dp(root, RIGHT, 0)

        return result


tests = [
    [build_tree_from_list([1,null,1,null,1,1,null,null,1]), 3],
    [build_tree_from_list([6,9,7,3,null,2,8,5,8,9,7,3,9,9,4,2,10,null,5,4,3,10,10,9,4,1,2,null,null,6,5,null,null,null,null,9,null,9,6,5,null,5,null,null,7,7,4,null,1,null,null,3,7,null,9,null,null,null,null,null,null,null,null,9,9,null,null,null,7,null,null,null,null,null,null,null,null,null,6,8,7,null,null,null,3,10,null,null,null,null,null,1,null,1,2]), 5],
    [build_tree_from_list([1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]), 3],
    [build_tree_from_list([1,1,1,null,1,null,null,1,1,null,1]), 4],
    [build_tree_from_list([1]), 0],
]

run_functional_tests(Solution().longestZigZag, tests)
