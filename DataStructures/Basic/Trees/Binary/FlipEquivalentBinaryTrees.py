"""
https://leetcode.com/problems/flip-equivalent-binary-trees/

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.



Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false


Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].
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


# Runtime: 26 ms, faster than 98.03% of Python3 online submissions for Flip Equivalent Binary Trees.
# Memory Usage: 13.8 MB, less than 81.72% of Python3 online submissions for Flip Equivalent Binary Trees.
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or \
               self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)


tests = [
    [
        build_tree_from_list([1,2,3,4,5,6,null,null,null,7,8]),
        build_tree_from_list([1,3,2,null,6,4,5,null,null,null,null,8,7]),
        True
    ],
    [
        None, None, True
    ],
    [
        None,
        build_tree_from_list([1]),
        False
    ]
]

run_functional_tests(Solution().flipEquiv, tests)
