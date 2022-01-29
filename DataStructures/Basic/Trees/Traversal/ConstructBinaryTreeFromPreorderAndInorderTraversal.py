"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3772/
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Common.DataTypes.Leetcode import TreeNode
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 160 ms, faster than 36.58% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 19.2 MB, less than 62.35% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#
#         def impl(pre_b: int, pre_e: int, in_b: int, in_e: int) -> TreeNode:
#             if pre_b == pre_e:
#                 return None
#             val = preorder[pre_b]
#             root = TreeNode(val)
#             m = inorder.index(val, in_b, in_e)
#             left_end = pre_b + 1 + m - in_b
#             root.left = impl(pre_b+1, left_end, in_b, m)
#             root.right = impl(left_end, pre_e, m+1, in_e)
#             return root
#
#         return impl(0, len(preorder), 0, len(inorder))


# Runtime: 52 ms, faster than 94.26% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
# Memory Usage: 19.4 MB, less than 55.02% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        inorder_index = {v: i for i, v in enumerate(inorder)}

        def impl(pre_b: int, pre_e: int, in_b: int, in_e: int) -> TreeNode:
            if pre_b == pre_e:
                return None
            val = preorder[pre_b]
            root = TreeNode(val)
            m = inorder_index[val]
            left_end = pre_b + 1 + m - in_b
            root.left = impl(pre_b+1, left_end, in_b, m)
            root.right = impl(left_end, pre_e, m+1, in_e)
            return root

        return impl(0, len(preorder), 0, len(inorder))


tests = [
    [
        [3,9,20,15,7],
        [9,3,15,20,7],
        TreeNode(3,
                 TreeNode(9),
                 TreeNode(20,
                          TreeNode(15),
                          TreeNode(7)))
    ],
    [
        [-1],
        [-1],
        TreeNode(-1)
    ]
]


run_functional_tests(Solution().buildTree, tests)